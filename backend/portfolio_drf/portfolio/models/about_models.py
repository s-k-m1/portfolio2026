from django.db import models

class AboutInfo(models.Model):
    title = models.CharField(max_length=200, default="About Me")
    subtitle = models.CharField(max_length=200, default="Full Stack Developer")
    description = models.TextField()
    professional_summary = models.TextField()
    cv_file = models.FileField(upload_to='cv/', blank=True, null=True)

    class Meta:
        verbose_name_plural = "About Info"

    def __str__(self):
        return self.title

class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('frontend', 'Frontend'),
        ('backend', 'Backend'),
    ]
    name = models.CharField(max_length=100)
    percent = models.IntegerField(default=0)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)

    def __str__(self):
        return f"{self.name} ({self.category})"

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    link = models.URLField(blank=True, default="#")
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.title