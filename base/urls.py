from django.urls import path
from base import views

urlpatterns = [

    path('', views.contact_view, name='contact'),
]
