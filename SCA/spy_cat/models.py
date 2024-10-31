from django.db import models


class SpyCat(models.Model):
    name = models.CharField(max_length=128)
    experience = models.SmallIntegerField(help_text='Years of experience')
    breed = models.CharField(max_length=64)
    salary = models.PositiveIntegerField()

    def __str__(self):
        return self.name
