from email.policy import default
from termios import PENDIN
from django.db import models


class Appointment(models.Model):
    PENDING = 'PENDING'
    ABSENT = 'ABSENT'
    PERFORMED = 'PERFORMED'
    CANCELLED = 'CANCELLED'
    APPOINTMENT_STATUS = (
        (PENDING, "Appointment created and waiting for status change"),
        (ABSENT, "Patient's absent"),
        (PERFORMED, "The appointment was performed successfully"),
        (CANCELLED, "The appointment was cancelled by the doctor or patient"),
    )

    doctor_id = models.BigIntegerField(
        null=False,
        help_text="Doctor's appointment id",
    )
    patient_id = models.BigIntegerField(
        null=False,
        help_text="Patient's appointment id",
    )
    date = models.DateTimeField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        null=False,
        blank=False,
        default=PENDING,
        choices=APPOINTMENT_STATUS
    )

    class Meta:
        db_table = "appointment"
        ordering = ('-created_at',)
        verbose_name = 'Appointment'
        verbose_name_plural = 'Appointments'
