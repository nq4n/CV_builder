from django.db import models

# Create your models here

from django.db import models

class CV(models.Model):
    # Personal Information
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)

    # Education Information
    degree = models.CharField(max_length=100)
    university = models.CharField(max_length=100)
    graduation_year = models.PositiveIntegerField()

    # Skills
    skills = models.TextField(blank=True, null=True)  # Store comma-separated skills

    def __str__(self):
        return self.name

class WorkExperience(models.Model):
    # Relationship to the CV model
    cv = models.ForeignKey(CV, on_delete=models.CASCADE, related_name='experiences')

    # Work Experience Fields
    job_title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    years_worked = models.CharField(max_length=50)  # Use a string to allow flexible input (e.g., "2 years" or "2019-2021")

    def __str__(self):
        return f"{self.job_title} at {self.company}"
