from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from apps.jobs.models import (Job, 
                     Application,
                     JobCategory,
                     Review,
                     JobInquiry)

from apps.jobs.serializers import (JobSerializer, 
                          ApplicationSerializer,
                          JobCategorySerializer,
                          ReviewSerializer,
                          JobInquirySerializer)

from PyPDF2 import PdfReader
from docx import Document


class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
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

        allowed_types = [
            "application/pdf",
            "application/msword",
            "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        ]
        if file.content_type not in allowed_types:
            return Response({"error": "Invalid file type."}, status=status.HTTP_400_BAD_REQUEST)

        job.resume = file
        job.save()

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


class JobCategoryViewSet(viewsets.ModelViewSet):
    queryset = JobCategory.objects.all()
    serializer_class = JobCategorySerializer
    

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class JobInquiryViewSet(viewsets.ModelViewSet):
    queryset = JobInquiry.objects.all()
    serializer_class = JobInquirySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
