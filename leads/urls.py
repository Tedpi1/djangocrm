from django.urls import path
from .views import home

# from .views import home

urlpatterns = [
    path('', home),
]