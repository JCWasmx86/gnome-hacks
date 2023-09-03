from datetime import datetime

from django.contrib.auth.models import User
from django.core.validators import MaxLengthValidator, ValidationError
from django.db import models


def empty_array():
    return []


class Location(models.Model):
    description = models.TextField(
        max_length=1024 * 1024 * 4, validators=[MaxLengthValidator(1024 * 1024 * 4)]
    )
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    address = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name


class Hackfest(models.Model):
    organizer = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    location = models.ForeignKey(Location, on_delete=models.PROTECT)
    title = models.CharField(max_length=200)
    start = models.DateTimeField(default=datetime.now)
    end = models.DateTimeField(default=datetime.now)
    description = models.TextField(
        max_length=1024 * 1024 * 4, validators=[MaxLengthValidator(1024 * 1024 * 4)]
    )

    def clean(self):
        if self.start > self.end:
            raise ValidationError("Start must be before the end")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)


class TrustedUser(models.Model):
    hackfest = models.ForeignKey(Hackfest, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)


class Attendee(models.Model):
    hackfest = models.ForeignKey(Hackfest, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return str(self.user)
