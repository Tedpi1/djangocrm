from django.urls import path
from .views import(
    leadListView, LeadDetailView, LeadUpdateView, LeadDeleteView, LeadCreateView
)
app_name="leads"
# from .views import home

urlpatterns = [
    path('', leadListView.as_view(), name='lead-list'),
    path('<int:pk>/', LeadDetailView.as_view(), name='lead-detail'),
    path('<int:pk>/update/', LeadUpdateView.as_view(), name='lead-update'),
    path('<int:pk>/delete/', LeadDeleteView.as_view(), name='lead-delete'),
    path('create/', LeadCreateView.as_view(), name='lead-create'),
    
]