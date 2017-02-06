from django.conf.urls import include, url
from views import *

urlpatterns = [
    url(r'^task/$', TaskView.as_view(), name='task'),
	url(r'^assign/$', AssignmentView.as_view(), name='assign'),
	url(r'^buddy/assign/$', BuddyView.as_view(), name='buddy_detail'),

]