from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=255)  # Event title
    description = models.TextField(blank=True, null=True)  # Optional description
    date = models.DateField()  # Event date
    created_at = models.DateTimeField(auto_now_add=True)  # Auto timestamp when created

    def __str__(self):
        return self.title  # Display event title in Django Admin
