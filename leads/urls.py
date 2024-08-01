from django.urls import path
from .views import lead_list, test, lead_detail, lead_create
#app_name="leads"
# from .views import home

urlpatterns = [
    path('', lead_list),
    path('test/', test),
    path('<int:pk>/', lead_detail),
    path('create/', lead_create),
]