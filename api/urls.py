from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = format_suffix_patterns([
    url(r'^fetch/$', views.BuddyList.as_view(), name='buddy-list'),
    url(r'^assign/$', views.BuddyPost.as_view(), name='buddy-assign'),
    # url(r'^(?P<buddy_id>[\d+])/disable/$',views.disable,name="buddy-disable"),
    url(r'^(?P<buddy_id>[\d+])/detail/$', views.BuddyDetail.as_view(), name='buddy-detail'),
    #url(r'^post/$',views.buddy_list,name="buddy-post"),
])