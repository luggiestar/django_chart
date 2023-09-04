from django.db import models

# Create your models here.
class Club(models.Model):
    name = models.CharField(max_length=60, unique=True)
    amount = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name