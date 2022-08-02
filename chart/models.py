from django.db import models

class Gender:
    MALE = 1
    FEMALE = 2
    OTHERS = 3

    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHERS, 'Others'),
    )


class Staff(models.Model):
    name = models.CharField(max_length=100)
    gender = models.IntegerField(choices=Gender.GENDER_CHOICES)
    age = models.IntegerField()
    salary = models.FloatField()
