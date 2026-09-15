from rest_framework import generics
from .models import JobApplication
from .serializer import JobApplicationSerializer
from django.core.mail import send_mail
from django.db.models import Count
from rest_framework.views import APIView
from rest_framework.response import Response


class JobApplicationListCreateView(generics.ListCreateAPIView):
    serializer_class = JobApplicationSerializer

    def get_queryset(self):
        queryset = JobApplication.objects.all()

        candidate = self.request.query_params.get('candidate')

        if candidate:
            queryset = queryset.filter(candidate_id=candidate)

        return queryset

    def perform_create(self, serializer):

        application = serializer.save()

        employer_email = application.job.employer.email

        send_mail(
            subject='Job Application',
            message='Job Application created successfully',
            from_email='ramgupta639225@gmail.com',
            recipient_list=[employer_email], )



class JobApplicationDetailView(generics.RetrieveUpdateAPIView):
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationSerializer



class ApplicationStatisticsView(APIView):

    def get(self, request):
        total_applications = JobApplication.objects.count()

        pending = JobApplication.objects.filter(
            status='Pending'
        ).count()

        reviewed = JobApplication.objects.filter(
            status='Reviewed'
        ).count()

        shortlisted = JobApplication.objects.filter(
            status='Shortlisted'
        ).count()

        rejected = JobApplication.objects.filter(
            status='Rejected'
        ).count()

        accepted = JobApplication.objects.filter(
            status='Accepted'
        ).count()

        return Response({
            'total_applications': total_applications,
            'pending': pending,
            'reviewed': reviewed,
            'shortlisted': shortlisted,
            'rejected': rejected,
            'accepted': accepted,
        })



