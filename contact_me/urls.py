from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact_me),
    path('thank-you', views.thank_you, name='thank-you')
]
