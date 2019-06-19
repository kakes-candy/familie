from django.db import models
from django.contrib.auth.models import User


class Profiel(models.Model):
    voornaam = models.CharField(max_length=50)
    achternaam = models.CharField(max_length=50)
    tussenvoegsels = models.CharField(max_length=50, blank=True, null=True)
    geboortedatum = models.DateTimeField()
    geboorteplaats = models.CharField(max_length=100, blank=True, null=True)
    mijn_vader = models.OneToOneField(
        "self", blank=True, null=True, on_delete=models.SET_NULL, related_name="vader"
    )
    mijn_moeder = models.OneToOneField(
        "self", blank=True, null=True, on_delete=models.SET_NULL, related_name="moeder"
    )
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

