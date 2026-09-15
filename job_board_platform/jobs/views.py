from rest_framework import generics
from .models import Job
from .serializer import JobSerializer

class JobListCreateView(generics.ListCreateAPIView):
    serializer_class = JobSerializer

    def get_queryset(self):
        queryset = Job.objects.all()

        search = self.request.query_params.get('search')
        location = self.request.query_params.get('location')
        job_type = self.request.query_params.get('job_type')

        if search:
            queryset = queryset.filter(title__icontains=search)

        if location:
            queryset = queryset.filter(location__icontains=location)

        if job_type:
            queryset = queryset.filter(job_type__icontains=job_type)

        return queryset

