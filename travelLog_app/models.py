from django.db import models

class Place(models.Model):
    place_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=50)  
    description = models.TextField()
    opening_hours = models.TimeField()
    closing_hours = models.TimeField()
    image = models.ImageField(upload_to='place_images/')

    def __str__(self):
        return self.name
