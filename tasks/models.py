from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class Task(models.Model):

    STATUS = [
        ('doing', 'Doing'),
        ('done', 'Done')
    ]

    title = models.CharField(max_length=256)
    description = models.CharField(max_length= 1024)
    done = models.CharField(max_length=64, choices=STATUS)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title