from django.conf.urls import url

urlpatterns=[
	url(r'^sign_up/$','user_profile.views.signup',name="signup"), 
	url(r'^$','user_profile.views.login_view',name="login"),
	url(r'^logout/$','user_profile.views.user_logout',name="logout"),
	url(r'^profile/$','user_profile.views.profile',name="logged_in_user"),

]