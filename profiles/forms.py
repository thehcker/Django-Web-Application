from django import forms
from profiles.models import Album

class AlbumForm(forms.ModelForm):
	class Meta:
		model = Album
		fields = ('artist','album_title','album_logo')

from django.contrib.auth.models import User

class signupform(forms.ModelForm):
	class Meta:
		model = User
		fields = ('email','username','password')