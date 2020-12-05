from django.db import models


# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    image = models.ImageField()

    def __str__(self):
        return self.first_name

class Intro(models.Model):
    Male = 'M'
    Female = 'F'
    Both = 'M/F'
    CHOICE_IN_PREFERENCE = [
        (Male, 'M'),
        (Female, 'F'),
        (Both, 'M/F'),
    ]
    preference = models.CharField(
        max_length=3,
        choices=CHOICE_IN_PREFERENCE,

    )
    interests = models.CharField(max_length=200)
    bio_message = models.TextField()


class About(models.Model):
    age = models.IntegerField()
    height = models.IntegerField()
    location = models.CharField(max_length=100)
