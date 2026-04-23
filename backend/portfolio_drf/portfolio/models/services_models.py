from django.db import models

class Service(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    # icon_name will store strings like 'Code', 'Layout', 'Database'
    icon_name = models.CharField(max_length=100) 
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title