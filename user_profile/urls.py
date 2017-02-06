from django.conf.urls import url

urlpatterns=[
	# sign_up url 
	url(r'^sign_up/$',\
			'user_profile.views.signup',name="signup"), 

	# home page url or login page url
	url(r'^$',\
		'user_profile.views.login_view',name="login"),

	# logout url
	url(r'^logout/$',\
		'user_profile.views.user_logout',name="logout"),

	# user profile dashboard after making a login
	url(r'^profile/$',\
		'user_profile.views.profile',name="logged_in_user"),

]