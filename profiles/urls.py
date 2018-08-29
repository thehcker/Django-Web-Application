from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('homee/', views.homee, name='homee'),
    path('index/', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('today/', views.today, name='today'),
    path('contact/', views.contact, name='contact'),
    path('logo/', views.logo, name='logo'),
    path('login/', views.logo, name='login'),
    path('signup/', views.logo, name='signup'),
    path('logout/', views.logo, name='logout'),
    path('song/', views.song, name='song'),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)