from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50)
    x = models.IntegerField()
    y = models.IntegerField()
    description = models.CharField(max_length=255, null=True)

    def __str__(self):
        return f"{self.name}: ({self.x}, {self.y})"
