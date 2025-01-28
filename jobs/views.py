from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from .models import Job, Application
from .serializers import JobSerializer, ApplicationSerializer
from rest_framework.decorators import action
from .serializers import JobSerializer
from PyPDF2 import PdfReader
from docx import Document
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter



class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [permissions.IsAuthenticated]
        # Add filter backends
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

    # Specify the fields available for filtering
    filterset_fields = ['location', 'job_type', 'category']

    # Specify the fields available for search
    search_fields = ['title', 'description']

    # Specify the fields available for ordering
    ordering_fields = ['created_at', 'title']
    ordering = ['-created_at']  # Default ordering by newest first

    def perform_create(self, serializer):
        # Automatically assign the employer (user) who creates the job
        serializer.save(employer=self.request.user)

    @action(detail=True, methods=['get'])
    def applications(self, request, pk=None):
        job = self.get_object()
        applications = job.applications.all()
        serializer = ApplicationSerializer(applications, many=True)
        return Response(serializer.data)


class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # Automatically assign the candidate (user) who applies for the job
        serializer.save(candidate=self.request.user)


class FileUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        """
        Handle file uploads and extract content if applicable.
        """
        job_id = kwargs.get("job_id")
        try:
            job = Job.objects.get(id=job_id)
        except Job.DoesNotExist:
            return Response({"error": "Job not found."}, status=status.HTTP_404_NOT_FOUND)

        file = request.FILES.get("file")
        if not file:
            return Response({"error": "No file uploaded."}, status=status.HTTP_400_BAD_REQUEST)

        # Validate file type
        allowed_types = [
            "application/pdf",
            "application/msword",
            "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        ]
        if file.content_type not in allowed_types:
            return Response({"error": "Invalid file type."}, status=status.HTTP_400_BAD_REQUEST)

        # Save the file to the Job model
        job.resume = file
        job.save()

        # Extract content if it's a PDF or DOCX file
        extracted_content = None
        try:
            if file.name.endswith(".pdf"):
                extracted_content = self.extract_text_from_pdf(file)
            elif file.name.endswith(".docx"):
                extracted_content = self.extract_text_from_docx(file)
        except Exception as e:
            return Response(
                {"error": f"Error extracting content: {str(e)}"}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        # Return a detailed response
        return Response(
            {
                "message": "File uploaded and processed successfully.",
                "file_url": job.resume.url,
                "file_name": file.name,
                "file_size": file.size,
                "extracted_content": extracted_content,
            },
            status=status.HTTP_200_OK,
        )

    def extract_text_from_pdf(self, file):
        """
        Extract text from a PDF file.
        """
        reader = PdfReader(file)
        text = ''
        for page in reader.pages:
            text += page.extract_text()
        return text

    def extract_text_from_docx(self, file):
        """
        Extract text from a DOCX file.
        """
        doc = Document(file)
        return '\n'.join([paragraph.text for paragraph in doc.paragraphs])

