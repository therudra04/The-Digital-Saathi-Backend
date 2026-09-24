from django.conf import settings
from django.core.mail import send_mail
from rest_framework import generics

from .models import ContactMessage
from .serializers import ContactMessageSerializer


class ContactMessageCreateAPIView(generics.CreateAPIView):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer

    def perform_create(self, serializer):
        contact = serializer.save()

        try:
            send_mail(
                subject=f"New Website Inquiry from {contact.name}",
                message=f"""
New inquiry received from The Digital Saathi website.

Name: {contact.name}
Email: {contact.email}
Phone: {contact.phone}
Service: {contact.service}

Message:
{contact.message}
""",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.CONTACT_RECEIVER_EMAIL],
                reply_to=[contact.email],
                fail_silently=False,
            )

        except Exception as error:
            print("Email sending failed:", error)