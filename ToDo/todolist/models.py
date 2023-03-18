from django.db import models
from django.utils import timezone


def due_date():
    return timezone.now() + timezone.timedelta(days=7)


# Create your models here.
class Task(models.Model):
    STATUS = [
        ("not started yet", "not started yet"),
        ("in progres...", "in progress"),
        ("pending", "pending"),
        ("done", "done"),
    ]

    CATEGORY = [
        ("new", "unassigned"),
        ("urgent and important", "urgent and important"),
        ("not urgent and important", "urgent and not important"),
        ("urgent but not important", "urgent but not important"),
        ("not urgent and not important", "not urgent and not important"),
    ]

    ID = models.AutoField(primary_key=True)
    user = models.TextField
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    category = models.CharField(max_length=50, choices=CATEGORY, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=50, choices=STATUS, null=True)
    due_date = models.DateTimeField(default=due_date)

    def __str__(self) -> str:
        return f"{self.title} {self.category} {self.status}."

    class Meta:
        ordering = ["due_date"]
