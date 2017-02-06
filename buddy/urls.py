from django.conf.urls import include, url
from views import *

urlpatterns = [
	# create a new assignment for buddy
    url(r'^task/$', TaskView.as_view(), name='task'),
	url(r'^assign/$', AssignmentView.as_view(), name='assign'),

	# create a new buddy
	url(r'^buddy/create/$', BuddyView.as_view(), name='buddy_create'),

]