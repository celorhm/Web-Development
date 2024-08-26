from .views import SignupView,ProfilePageView
from django.urls import path

app_name = 'accounts'

urlpatterns = [
    path("signup/", SignupView.as_view(), name="signup"), 
    path("profile-page/", ProfilePageView.as_view(), name="profile-page")
]
