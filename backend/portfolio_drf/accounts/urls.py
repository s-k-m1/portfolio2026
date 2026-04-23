from django.urls import path
from .views import ContactInquiryListCreate 

urlpatterns = [
    path('contact/', ContactInquiryListCreate.as_view(), name='contact-inquiry'),
]