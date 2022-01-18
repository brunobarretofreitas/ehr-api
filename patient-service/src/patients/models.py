from random import choice
from django.db import models


class Patient(models.Model):
    first_name = models.CharField(
        max_length=100,
        null=False,
        blank=False,
    )
    last_name = models.CharField(
        max_length=100,
        null=False,
        blank=False,
    )
    birth_date = models.DateField(
        null=False
    )
    gender = models.CharField(
        max_length=1,
        null=False,
        blank=False,
        choices=(
            ('F', 'Female'),
            ('M', 'Male'),
        )
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'patients'
        ordering = ('-id',)

    def __str__(self):
        return self.first_name
