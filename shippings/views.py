from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import ClientForm


def get_name(request):

    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('thanks.html')

    else:
        form = ClientForm()

    return render(request, 'template.html', {'form': form})
