from django.db import models

# Create your models here.

class Dog(models.Model):
    nazwa = models.CharField(max_length=120)
    opis = models.TextField()
    gotowe = models.BooleanField(default=False)

    def __str__(self):
        return self.nazwa

