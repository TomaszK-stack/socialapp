from django.urls import path, include
from .views import ProfileView


urlpatterns = [
    path('profile', ProfileView.as_view(), name = 'Profile_view')


]
