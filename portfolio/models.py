from django.db import models


class Experience(models.Model):
    company = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self):
        return self.company


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    tech_stack = models.CharField(max_length=200)
    
    def __str__(self):
        return self.title


class Certification(models.Model):
    name = models.CharField(max_length=200)
    issuer = models.CharField(max_length=200)
    link = models.URLField()
    
    def __str__(self):
        return self.name


class Education(models.Model):
    institution = models.CharField(max_length=200)
    duration = models.CharField(max_length=100)
    qualification = models.CharField(max_length=200)
    
    def __str__(self):
        return self.institution


class Skills(models.Model):
    skill_name = models.CharField(max_length=20)
    skill_level = models.IntegerField()
    icon = models.ImageField(upload_to='skills/icons/', null=True, blank=True)

    
    def __str__(self):
        return self.skill_name
    

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"

