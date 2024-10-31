from django.db import models


class Mission(models.Model):
    cat = models.ForeignKey('spy_cat.SpyCat', on_delete=models.CASCADE, null=True)
    is_complete = models.BooleanField(default=False)


class Target(models.Model):
    name = models.CharField(max_length=128)
    country = models.CharField(max_length=256)
    notes = models.TextField()
    mission = models.ForeignKey(Mission, on_delete=models.CASCADE, related_name='targets')
    is_complete = models.BooleanField(default=False)

    def __str__(self):
        return self.name
