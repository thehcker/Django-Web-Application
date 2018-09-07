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
	#userId = models.IntegerField(null=True)
	artist = models.CharField(max_length=120)
	album_title = models.CharField(max_length =120)
	genre = models.CharField(max_length = 100, default = 'mylocationdefault')
	album_logo = models.ImageField(max_length = 120, blank = True)
	def __str__(self):
		return self.album_title


class Song(models.Model):
	#userId = models.IntegerField(null=True)
	#album = models.ForeignKey(Album,on_delete = models.CASCADE,null=True)
	song = models.CharField(max_length=120)
	genre = models.TextField(max_length =120)
	producer = models.TextField(max_length = 100, default = 'mylocationdefault')
	#year = models.TextField(max_length = 120, blank = True)
	def __str__(self):
		return self.song

class titledeed(models.Model):
	#userId = models.ForeignKey(titleDeed,on_delete = models.CASCADE)
	owners_name = models.CharField(max_length=30)
	ref_no = models.CharField(max_length =25)
	demographic = models.CharField(max_length = 30)
	size = models.CharField(max_length = 20)

	def __str__(self):
		return self.owners_name
