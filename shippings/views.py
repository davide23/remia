from django.shortcuts import render

from .forms import ClientForm
from .models import Client

def get_name(request):

    if request.method == 'POST':
        data = {
            'full_name': request.POST['name'],
            'street_and_number': request.POST['address'],
            'postcode': request.POST['postal-code'],
            'city': request.POST['city'],
            'origin': request.POST['origin'] or 'Unknown',
        }

        form = ClientForm(data=data)
        form.save()

        if form.is_valid():
            if Client.objects.filter(full_name__iexact=request.POST['name']).count() > 0:
                count = 1
            if Client.objects.filter(street_and_number__iexact=request.POST['address']) and \
                    Client.objects.filter(postcode=request.POST['postal-code']):
                form.save()
            return render(request, template_name='thanks.html')

    else:
        form = ClientForm()

    return render(request, 'index.html', {'form': form})
