from rest_framework import serializers
from buddy.models import BuddyDetail

class BuddyDetailSerializer(serializers.ModelSerializer):
	class Meta:
		model=BuddyDetail
		fields = '__all__'



