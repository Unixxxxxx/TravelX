from django.shortcuts import render, redirect 
from .forms import ContactForm
from django.http import HttpResponseForbidden

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def hone(request):
    return render(request, 'home.html')
def Service(request):
    return render(request, 'Service.html')

def service(request):
    return render(request, 'service.html')

def secure_view(request):
    if not request.user.is_superuser:
        return render(request, '404.html', status=403)
    return render(request, 'index.html')

def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')
        else:
            form = ContactForm()
        return render(request,'contact.html', {'form':form})


def custom_page_not_found(request, exception):
    return render(request, '404.html', status=404)

def custom_permission_denied(request, exception=None):
    return render(request, '404.html', status=403)
