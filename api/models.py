from django.db import models
from django.contrib.auth.models import User

class Location(models.Model):
    
    name = models.CharField(max_length=100)        
    category = models.CharField(max_length=50)    
    cost = models.IntegerField()                   
    time_needed = models.FloatField(default=2.0)  

    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.name
    
class Trip(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    locations = models.ManyToManyField(Location)
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Trip for {self.user.username}"