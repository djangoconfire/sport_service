from buddy.models import BuddyDetail
from serializers import BuddyDetailSerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view


# fetching list of buddies
class BuddyList(generics.ListAPIView):
    queryset = BuddyDetail.objects.all()
    serializer_class = BuddyDetailSerializer

# create a new buddy
class BuddyPost(generics.ListCreateAPIView):
    queryset = BuddyDetail.objects.all()
    serializer_class = BuddyDetailSerializer
    permission_classes = (permissions.IsAdminUser,)


# Delete a buddy
class BuddyDisable(generics.DestroyAPIView):
    queryset = BuddyDetail.objects.all()
    serializer_class = BuddyDetailSerializer 
    lookup_field="buddy_id"  


# getting detail of a particular buddy
class BuddyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BuddyDetail.objects.all()
    serializer_class = BuddyDetailSerializer 
    lookup_field="buddy_id"  



  