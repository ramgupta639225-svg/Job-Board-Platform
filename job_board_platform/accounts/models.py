from django.db import models


class Employer(models.Model):
    company_name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    description = models.TextField()
    location = models.CharField(max_length=200)
    website = models.URLField(blank=True, null=True)


    def __str__(self):
        return self.company_name


class Candidate(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    skills = models.TextField()
    experience = models.CharField(max_length=100)


    def __str__(self):
        return self.name
