from rest_framework import serializers
from buddy.models import BuddyDetail,BatchDetail

class BuddySerializer(serializers.ModelSerializer):
	class Meta:
		model=BuddyDetail
		fields = '__all__'



class BatchSerializer(serializers.ModelSerializer):
	class Meta:
		model=BatchDetail
		fields = '__all__'



