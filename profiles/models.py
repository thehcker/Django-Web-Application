from django.db import models

# Create your models here.
class profiles(models.Model):
	name = models.CharField(max_length=120)
	description = models.TextField(max_length =120)
	location = models.TextField(max_length = 100, default = 'mylocationdefault')
	job = models.TextField(max_length = 120, blank = True)
	def __init__(self):
		return self.name

class Album(models.Model):
	artist = models.CharField(max_length=120)
	album_title = models.CharField(max_length =120)
	genre = models.CharField(max_length = 100, default = 'mylocationdefault')
	album_logo = models.ImageField(max_length = 120, blank = True)
	def __unicode__(self):
		return self.artist

class Song(models.Model):
	song = models.CharField(max_length=120)
	genre = models.TextField(max_length =120)
	producer = models.TextField(max_length = 100, default = 'mylocationdefault')
	#year = models.TextField(max_length = 120, blank = True)
	def __unicode__(self):
		return self.producer
