from django.urls import path 
from .views import index, contact_view, secure_view, about

urlpatterns = [
        path('',index, name='index'),
        path('', contact_view, name='contact'),
        path('about/', about, name='about' ),
        path('secure/', secure_view, name='secure'),
        ]
