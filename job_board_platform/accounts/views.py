from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Employer, Candidate


class UserManagementView(APIView):

    def get(self, request):
        employers = Employer.objects.all()
        candidates = Candidate.objects.all()

        employer_data = [
            {
                'id': employer.id,
                'company_name': employer.company_name,
                'email': employer.email,
                'location': employer.location,
            }
            for employer in employers
        ]

        candidate_data = [
            {
                'id': candidate.id,
                'name': candidate.name,
                'email': candidate.email,
                'phone': candidate.phone,
                'skills': candidate.skills,
                'experience': candidate.experience,
            }
            for candidate in candidates
        ]

        return Response({
            'total_employers': employers.count(),
            'total_candidates': candidates.count(),
            'employers': employer_data,
            'candidates': candidate_data,
        })

