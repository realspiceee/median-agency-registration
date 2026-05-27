from django.db import models


class User(models.Model):
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    password_hash = models.CharField(max_length=255)

    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.full_name


class Event(models.Model):
    title = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    event_date = models.DateField()
    description = models.TextField()

    class Meta:
        db_table = 'events'

    def __str__(self):
        return self.title


class Registration(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='registrations'
    )

    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name='registrations'
    )

    registration_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'registrations'

    def __str__(self):
        return f"{self.user.full_name} - {self.event.title}"
