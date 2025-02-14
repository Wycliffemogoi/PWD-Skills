from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/create/', views.profile_create, name='profile_create'),
    path('profile/update/', views.profile_update, name='profile_update'),  # New URL for profile update

]