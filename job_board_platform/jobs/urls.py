from .views import JobListCreateView
from django.urls import path


urlpatterns = [
    path('', JobListCreateView.as_view(), name='job-list-create')
]




