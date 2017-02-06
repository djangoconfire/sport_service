from buddy.models import BuddyDetail
from serializers import BuddyDetailSerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view



class BuddyList(generics.ListAPIView):
    queryset = BuddyDetail.objects.all()
    serializer_class = BuddyDetailSerializer

class BuddyPost(generics.ListCreateAPIView):
    queryset = BuddyDetail.objects.all()
    serializer_class = BuddyDetailSerializer
    # permission_classes = (permissions.IsAdminUser,)

    

class BuddyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BuddyDetail.objects.all()
    serializer_class = BuddyDetailSerializer 
    lookup_field="buddy_id"    


# class BuddyDisable(generics.RetrieveDestroyAPIView):
#     queryset = BuddyDetail.objects.all()
#     serializer_class = BuddyDetailSerializer 
#     lookup_field="buddy_id" 



# @api_view(['GET','Delete'])
# def buddy_disable(request,buddy_id):
#     """
#     List all buddies, or create a new buddy.
#     """

#     try:
#         buddy = BuddyDetail.objects.get(buddy_id=buddy_id)
#     except BuddyDetail.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)


#     if request.method == 'GET':
#         serializer = BuddyDetailSerializer(buddy)
#         return Response(serializer.data)

#     elif request.method == 'DELETE':
#         buddy.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)    

#     