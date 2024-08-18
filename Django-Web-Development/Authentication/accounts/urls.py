from .views import SignupView,HomePageView, ProfilePageView
from django.urls import path


urlpatterns = [
    path("signup/", SignupView.as_view(), name="signup"),
    path("",HomePageView.as_view(), name="home"),
    path("profile/", ProfilePageView.as_view(), name="user-profile")
]
