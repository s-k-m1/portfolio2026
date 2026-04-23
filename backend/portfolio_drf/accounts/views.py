from rest_framework import generics
from django.utils import timezone
from datetime import timedelta
from .models import ContactInquiry
from .serializers import ContactInquirySerializer

class ContactInquiryListCreate(generics.ListCreateAPIView):
    queryset = ContactInquiry.objects.all()
    serializer_class = ContactInquirySerializer

    def perform_create(self, serializer):
        serializer.save()

        # delete messages older than 30 days
        cutoff = timezone.now() - timedelta(days=30)
        ContactInquiry.objects.filter(created_at__lt=cutoff).delete()