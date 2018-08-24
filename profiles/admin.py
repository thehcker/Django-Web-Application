from django.contrib import admin

# Register your models here.
from .models import profiles
class profilesAdmin(admin.ModelAdmin):
	class Meta:
		model = profiles
admin.site.register(profiles,profilesAdmin)