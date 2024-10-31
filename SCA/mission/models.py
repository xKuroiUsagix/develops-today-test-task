from django.db import models


class Mission(models.Model):
    cat = models.ForeignKey('spy_cat.SpyCat', on_delete=models.CASCADE)


class Target(models.Model):
    name = models.CharField(max_length=128)
    country = models.CharField(max_length=256)
    notes = models.TextField()

    def __str__(self):
        return self.name


class MissionTarget(models.Model):
    mission = models.ForeignKey(Mission, on_delete=models.CASCADE)
    target = models.ForeignKey(Target, on_delete=models.CASCADE)
    is_complete = models.BooleanField(default=False)

    class Meta:
        unique_together = ['mission', 'target']

    def __str__(self):
        return f'{self.mission.cat} - {self.target}'
