from django.urls import path
from .views import JobApplicationListCreateView, ApplicationStatisticsView
from .views import JobApplicationDetailView




urlpatterns = [

    path('', JobApplicationListCreateView.as_view(), name='application-list-create'),
    path('<int:pk>/', JobApplicationDetailView.as_view(), name='application-detail'),
    path('statistics/', ApplicationStatisticsView.as_view(), name='application-statistics'),

]
