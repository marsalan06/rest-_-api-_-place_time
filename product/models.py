from django.db import models

# Create your models here.

class Product(models.Model):
    date=models.DateTimeField(auto_now_add= True)
    user_name=models.CharField(max_length=100)
    location_suggestion=models.TextField(blank=True, default='add location')
    date_suggestion=models.CharField(max_length=10)
    time_suggestion=models.DecimalField(max_digits=10,decimal_places=2)
    objects=models.Manager()
    def __str__(self):
        return self.user_name