from rest_framework.views import APIView
from rest_framework.response import Response
from ..models import Profile # can also do from ..models.my_model import Profile
from rest_framework import permissions, status

class NDAView(APIView):
    def get(self, request):
        """
        Update an nda's signed status
        request:
            vendorEventId
            signedBool
        """
        # permission_classes = (IsAuthenticated,)
        profile_qs = Profile.objects.all()

        user = request.user
        return Response('Success', status=status.HTTP_200_OK)
        pass