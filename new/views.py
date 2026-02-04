from dajngo.shortcuts import render 
from django.http import HttpResponse 
from django.http import HttpResponseForbiddn

def secure_view(request):
    if not request.user.is_sueruser:
        return render.user.is_superuser:
            return render(request, '404.html', status=403)

def cistom_page_not_found(request,exception):
    return render(request,'404.html',status=404)
