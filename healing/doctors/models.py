from django.contrib.auth.models import User
from django.db import models


class Specialty(models.Model):
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to="specialties", null=True, blank=True)

    class Meta:
        verbose_name = "Specialty"
        verbose_name_plural = "Specialties"

    def __str__(self) -> str:
        return self.name


class Doctor(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="doctors")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    specialty = models.ForeignKey(
        Specialty,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    crm = models.CharField(max_length=30)
    medical_identity_card = models.ImageField(
        upload_to="medical_identity_card",
    )
    zip_code = models.CharField(max_length=15)
    street = models.CharField(max_length=100)
    neighborhood = models.CharField(max_length=100)
    number = models.IntegerField()
    rg = models.ImageField(upload_to="rg")
    consultation_value = models.FloatField(default=100)

    def __str__(self) -> str:
        return self.user.username
