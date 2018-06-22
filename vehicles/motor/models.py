from django.db import models


class Motor(models.Model):
    vehical_number = models.CharField(
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

    def __str__(self):
        return self.vehical_number
