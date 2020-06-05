from django.db import models
from motel.models import motel
# Create your models here.

class rentingBoard(models.Model):
    idMotel = models.ForeignKey(motel,on_delete=models.CASCADE)
    content = models.TextField(max_length=1000)
    service = models.TextField(max_length=1000)

    def __str__(self):
        return self.idMotel