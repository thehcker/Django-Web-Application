from django import forms
from profiles.models import Album
from django.contrib.auth import User

class signupform(forms.ModelForm):
	class Meta:
		model = User
		fields = ('email','username','password')