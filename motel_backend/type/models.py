from django.db import models


# Create your models here.

class type(models.Model):
    typeName = models.CharField(max_length=50)

    def __str__(self):
        return self.typeName