from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name='MentalHealthAwareness'

urlpatterns=[
	#path('login/', auth_views.login, name='login'),
	#path('logout/', auth_views.logout, {'next_page':'MentalHealthAwareness:home'}, name='logout'),
	#path('signup/', views.SignUp, name='signup'),
	path('', views.HomePage, name='home'),
	path('help/', views.Help, name='help'),
	path('quotes/', views.Quotes, name='quotes'),
	path('videos/', views.Videos, name='videos'),
	path('post/', views.post_list, name='post_list'),
	path('post/new', views.post_new, name='post_new'),
]