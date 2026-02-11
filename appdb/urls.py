from django.urls import path 
from .views import index, contact_view, secure_view, about, service,Service

urlpatterns = [
        path('',index, name='index'),
        path('Service/',Service, name='Service'),
        path('',contact_view, name='contact'),
        path('servic/',service, name='service'),
        path('about/',about, name='about' ),
        path('secure/', secure_view, name='secure'),
        ]
