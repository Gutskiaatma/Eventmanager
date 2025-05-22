from django.db import models

# Create your models here.

class Event(models.Model):
    title = models.CharField(max_length=300)
    link = models.URLField()   


class EmailCapture(models.Model):
    email = models.EmailField()
    event_link = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.email} - {self.event_link}"