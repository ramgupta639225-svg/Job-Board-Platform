from django.db import models
from accounts.models import Employer

class Job(models.Model):

    JOB_TYPES = [
        ('Full Time', 'Full Time'),
        ('Part Time', 'Part Time'),
        ('Internship', 'Internship'),
        ('Remote', 'Remote'),
    ]

    employer = models.ForeignKey(
        Employer,
        on_delete=models.CASCADE,
        related_name='jobs'
    )

    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)

    salary = models.CharField(max_length=100)

    job_type = models.CharField(
        max_length=50,
        choices=JOB_TYPES
    )

    experience_required = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)

def __str__(self):
    return self.title
