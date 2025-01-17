from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse

def index(request):
    return render(request, 'home/index.html')
    
def about(request):
    return render(request, 'home/about.html')

def test_email(request):
    subject = "Test Email from Django"
    message = "This is a test email to verify SMTP settings."
    recipient_list = ["recipient@example.com"]  # Replace with the recipient's email
    send_mail(subject, message, None, recipient_list)
    return HttpResponse("Test email sent successfully!")

    