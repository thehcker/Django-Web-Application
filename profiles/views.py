from django.shortcuts import render,HttpResponse

from profiles.models import Album,Song

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

def song(request):
	songs = Song.objects.all()
	album = Album.objects.all()
	#context = locals()
	template = 'song.html'
	return render(request,template,{"Album":album,"Song":songs})

