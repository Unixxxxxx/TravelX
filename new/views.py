from django.shortcuts import render
from django.http import HttpResponseForbidden

def secure_view(request):
    if not request.user.is_superuser:
        return render(request, '403.html', status=403)
    return render(request, 'secure.html')

