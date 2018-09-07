from django.contrib.auth.decorators import login_required
from django.shortcuts import render,HttpResponse,redirect

from profiles.models import Album,Song,titledeed

# Create your views here.
def homee(request):
	return HttpResponse("Hello, World")
def index(request):
	return HttpResponse("I'm Here boo!")
def home(request):
	context = locals()
	template = 'home.html'
	return render(request,template,context)
def about(request):
	context = locals()
	template = 'about.html'
	return render(request,template,context)

def today(request):
	context = locals()
	template = 'today.html'
	return render(request,template,context)

def contact(request):
	context = locals()
	template = 'contact.html'
	return render(request,template,context)

def logo(request):
	context = locals()
	template = 'logo.html'
	return render(request,template,context)

def login(request):
	context = locals()
	template = 'login.html'
	return render(request,template,context)

def signup(request):
	context = locals()
	template = 'signup.html'
	return render(request,template,context)

def logout(request):
	context = locals()
	template = 'logout.html'
	return render(request,template,context)

def tablet(request):
	songs = Song.objects.all()
	album = Album.objects.all()
	template = 'tablet.html'
	return render(request,template,{"Song":songs,"Album":album})

def song(request):
	songs = Song.objects.all()
	template = 'song.html'
	return render(request,template,{"Song":songs})

def album(request):
	album = Album.objects.all()
	template = 'album.html'
	return render(request,template,{"Album":album})

@login_required
def userProfile(request):
	user = request.user
	context = {'user': user}
	template = 'profile.html'
	return render(request,template,context)

def titleDeed(request):
	template = 'titledeed.html'
	return render(request,template)

def Deed(request):
	owners_name = request.GET['owners_name']
	ref_no = request.GET['ref_no']
	demographic = request.GET['demographic']
	size = request.GET['size']
	#price = request.GET['price']
	title = titledeed.objects.create(
		owners_name = owners_name,
		ref_no = ref_no,
		demographic = demographic,
		size = size
		)
	title.save()
	return redirect('title')

def addalbum(request):
	template = 'addAlbum.html'
	return render(request,template)

def add(request):
	artist = request.GET['artist']
	album_title = request.GET['album_title']
	genre = request.GET['genre']
	album_logo = request.GET['album_logo']
	album = Album.objects.create(
		artist = artist,
		album_title = album_title,
		genre = genre,
		album_logo = album_logo
		)
	album.save()
	return redirect('album')

def newSong(request):
	template = 'newsong.html'
	return render(request,template)

def addsong(request):
	#album = request.GET['album']
	song = request.GET['song']
	genre = request.GET['genre']
	producer = request.GET['producer']
	songs = Song.objects.create(
		song = song,
		genre = genre,
		producer = producer
		)
	songs.save()
	return redirect('song')

