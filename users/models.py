from django.db import models

# Create your models here.


class User(models.Model):
    ROLE_CHOICES = [
        ('worker', 'Worker'),
        ('contractor', 'Contractor'),
    ]

    LANG_CHOICES = [
        ('en', 'English'),
        ('hi', 'Hindi'),
        ('te', 'Telugu'),
        ('ta', 'Tamil'),
    ]

    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    language = models.CharField(max_length=10, choices=LANG_CHOICES)
    location = models.CharField(max_length=200)

    # Profiles
    profile_image = models.ImageField(upload_to='profiles/', null=True, blank=True)
    bio = models.TextField(blank=True, null=True)

    # Worker only
    wage = models.IntegerField(null=True, blank=True)
    skills = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name