from django.db import models

# Create your models here.
class siteViewCounter(models.Model):
    total_views = models.IntegerField(default=0)
    
    def __str__(self):
        return f'total views : {str(self.total_views)}'