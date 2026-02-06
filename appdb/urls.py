from django.urls import path 
from .views import index, contact_view, secure_view

urlpatterns = [
        path('',index, name='index'),
        path('', contact_view, name='contact'),
        path('secure/', secure_view, name='secure'),
        ]
