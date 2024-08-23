from .models import UserProfile
from django.contrib.auth.forms import UserCreationForm

class SignupForm(UserCreationForm):
    class Meta:
        model = UserProfile
        fields = UserCreationForm.Meta.fields
