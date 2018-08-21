from django.forms import ModelForm

from .models import Client


class ClientForm(ModelForm):

    class Meta:
        model = Client
        fields = [
            'full_name',
            'street_and_number',
            'postcode',
            'city',
            'origin',
        ]
        labels = {
            'full_name': 'Volledige naam',
            'street_and_number': 'Straat + Huisnummer',
            'postcode': 'Postcode',
            'city': 'Plaats',
        }