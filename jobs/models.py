from django.db import models
from users.models import User
from django.utils import timezone


class Job(models.Model):
    title = models.CharField(max_length=200)
    salary = models.IntegerField()
    location = models.CharField(max_length=200)
    contractor = models.ForeignKey(User, on_delete=models.CASCADE)
    is_urgent = models.BooleanField(default=False)
    is_completed = models.BooleanField(default=False)
    timing = models.CharField(max_length=100, blank=True, null=True)
    job_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='job_images/', null=True, blank=True)

    # 🔥 Worker limit
    max_workers = models.IntegerField(default=1)

    # 📍 NEW: Map coordinates
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.title


class Application(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    worker = models.ForeignKey(User, on_delete=models.CASCADE)

    # 🔥 Hire status
    status = models.CharField(max_length=20, default="applied")

    # ⭐ Rating (1–5) and Reviews
    rating = models.IntegerField(null=True, blank=True)
    review = models.TextField(blank=True, null=True)
    contractor_rating = models.IntegerField(null=True, blank=True)
    contractor_review = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.worker.name} - {self.job.title}"