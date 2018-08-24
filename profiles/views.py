from django.shortcuts import render,HttpResponse

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

