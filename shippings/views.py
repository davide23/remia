from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import ClientForm


def get_name(request):

    if request.method == 'POST':

        data = {
            'full_name': request.POST['name'],
            'street_and_number': request.POST['address'],
            'postcode': request.POST['postal-code'],
            'city': request.POST['name'],
        }

        form = ClientForm(data=data)
        form.save()

        if form.is_valid():
            form.save()
            return render(request, template_name='thanks.html')

    else:
        form = ClientForm()

    return render(request, 'index.html', {'form': form})
