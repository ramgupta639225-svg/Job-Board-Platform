from django.urls import path
from .views import UserManagementView

urlpatterns = [
    path('users/', UserManagementView.as_view(), name='user-management'),
]

