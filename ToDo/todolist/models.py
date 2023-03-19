from django.db import models
from django.utils import timezone


def due_date():
    return timezone.now() + timezone.timedelta(days=7)


class Category(models.Model):
    name = models.CharField(max_length=255, default=None)

    # categories = models.CharField(max_length=50, choices=CATEGORY, default='unassigned')

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Status(models.Model):
    name = models.CharField(max_length=255, default=None)

    class Meta:
        verbose_name_plural = "Statuses"

    def __str__(self):
        return self.name


# Create your models here.
class Task(models.Model):
    ID = models.AutoField(primary_key=True)
    user = models.TextField
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, null=True, blank=True, default=None)
    due_date = models.DateTimeField(default=due_date)

    def __str__(self) -> str:
        return f"Title: {self.title}  Category:  {self.category}  Status: {self.status}."

    class Meta:
        ordering = ["due_date"]
