from django.db import models


class Client(models.Model):
    full_name = models.CharField(max_length=50, help_text="Volledige naam")
    street_and_number = models.CharField(max_length=300, help_text="Straat + Huisnummer")
    postcode = models.CharField(max_length=20, help_text="Postcode")
    city = models.CharField(max_length=200, help_text="Plaats")
    origin = models.CharField(max_length=200, default='Unknown')


