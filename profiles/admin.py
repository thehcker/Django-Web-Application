from django.contrib import admin
from . models import Album,Song

# Register your models here.

from .models import profiles
class profilesAdmin(admin.ModelAdmin):
	class Meta:
		model = profiles
	
admin.site.register(profiles)
admin.site.register(Album)
admin.site.register(Song)