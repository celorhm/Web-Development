from .views import SignupView,ProfilePageView
from django.urls import path

app_name = 'accounts'

urlpatterns = [
    path("signup/", SignupView.as_view(), name="signup"),
    path("profile/", ProfilePageView.as_view(), name="user-profile")
]
