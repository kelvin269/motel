from django.db import models

# Create your models here.
from django.utils import timezone

from type.models import type
from location.models import province, district, street, ward
from user.models import User

class motel(models.Model):
    owner = models.ForeignKey('user.User', related_name='motel', on_delete=models.CASCADE)
    type = models.ForeignKey(type, on_delete=models.CASCADE)
    province = models.ForeignKey(province, on_delete=models.CASCADE)
    district = models.ForeignKey(district, on_delete=models.CASCADE)
    ward = models.ForeignKey(ward, on_delete=models.CASCADE)
    street = models.ForeignKey(street, on_delete=models.CASCADE, blank=True)
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=20, decimal_places=3)
    create_at = models.DateField(default=timezone.now)
    update_at = models.DateField(default=timezone.now, blank=True)
    phone = models.IntegerField(default=0)
    arc = models.IntegerField(default=0)
    address = models.CharField(blank=True, max_length=100)

    def __str__(self):
        return self.title