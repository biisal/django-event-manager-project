from django.db import models
from django.contrib.auth.models import User
from eventApp.models import Event
# Create your models here.
class Attendee(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    registered_for = models.ForeignKey(Event, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.name} Registered for {self.registered_for}'