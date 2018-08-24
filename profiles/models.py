from django.db import models

# Create your models here.
class profiles(models.Model):
	name = models.CharField(max_length=120)
	description = models.TextField(max_length =120)
	location = models.TextField(max_length = 100, default = 'mylocationdefault')
	job = models.TextField(max_length = 120, blank = True)
	def __unicode__(self):
		return self.name
