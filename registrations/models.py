from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    event_date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.title


class Registration(models.Model):
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField()

    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name='registrations'
    )

    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.event.title}"