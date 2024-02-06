from django.db import models

# Create your models here.
class Task(models.Model):
    task_name = models.CharField(max_length=200)
    task_desc = models.TextField()
    task_created_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    image = models.ImageField(upload_to = 'media/',null=True)