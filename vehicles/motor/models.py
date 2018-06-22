from django.db import models
from accounts.models import User


class Motor(models.Model):
    vehicle_number = models.CharField(
        max_length=45,
        null=False
    )
    POLICY = (
        ('Y', 'YES'),
        ('N', 'NO')
    )
    policy = models.CharField(
        max_length=1,
        choices=POLICY,
        null=False
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.vehicle_number
