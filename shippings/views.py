from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render

from .forms import ClientForm


def get_name(request):

    if request.method == 'POST':

        data = {
            'full_name': request.POST['name'],
            'street_and_number': request.POST['address'],
            'postcode': request.POST['postal-code'],
            'city': request.POST['city'],
        }

        form = ClientForm(data=data)
        form.save()

        if form.is_valid():
            form.save()
            return redirect('https://www.remia.nl/')

    else:
        form = ClientForm()

    return render(request, 'index.html', {'form': form})
