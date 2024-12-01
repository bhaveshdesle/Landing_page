from django.db import models

# Create your models here.
# tourist/models.py
from django.db import models

class Destination(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    image = models.ImageField(upload_to='destinations/', null=True, blank=True)

    def __str__(self):
        return self.name

class Review(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name='reviews')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    rating = models.IntegerField(default=1)

    def __str__(self):
        return f"Review for {self.destination.name} by {self.name}"
from django.db import models

class TravelInfo(models.Model):
    from_location = models.CharField(max_length=100)
    to_location = models.CharField(max_length=100)
    travel_date = models.DateField()

    def __str__(self):
        return f"{self.from_location} to {self.to_location} on {self.travel_date}"

from django.db import models

class Booking(models.Model):
    from_location = models.CharField(max_length=100)
    to_location = models.CharField(max_length=100)
    travel_date = models.DateField()

    def __str__(self):
        return f"{self.from_location} to {self.to_location} on {self.travel_date}"

