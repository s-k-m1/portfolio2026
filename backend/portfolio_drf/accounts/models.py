from django.db import models

class ContactInquiry(models. Model):
    name= models.CharField(max_length=100)
    email= models.EmailField()
    subject= models.CharField(max_length=255, blank=True, null= True)
    message=models.TextField()
    
    # for Automatically saves the date and time when the record is created
    created_at = models.DateTimeField(auto_now_add= True)
    is_read =models.BooleanField(default=False)
    
    class Meta:
        verbose_name_plural = "Contact Inquiries"
        ordering = ['-created_at']  #for latest mesagess first
    
    def __str__(self):
        return f"{self.name} - {self.subject or 'No subject'}"