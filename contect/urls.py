from django.urls import path
from .views import info_form

urlpatterns = [
    path('info_form/', info_form, name='info_form'),
]

