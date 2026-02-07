from django.shortcuts import render, redirect
from .forms import InfoIDForm


def info_form(request):
    if request.method == 'POST':
        form = InfoIDForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('info_form')
    else:
        form = InfoIDForm()

    return render(request, 'form.html', {'form': form})

