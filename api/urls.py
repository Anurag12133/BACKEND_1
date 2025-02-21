from django.urls import path
from .views import JsonView

urlpatterns = [
    path('bfhl', JsonView.as_view(), name='bfhl'),
]