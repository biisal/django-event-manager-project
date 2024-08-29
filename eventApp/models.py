from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django_quill.fields import QuillField

# Create your models here.
class Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE , default=1)
    name = models.CharField(max_length=100)
    description = QuillField(default='Enter Your Description')
    date = models.DateField(default=timezone.now)
    event_date = models.DateField(default=timezone.now)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name