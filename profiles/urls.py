from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    #path('', views.home, name='home'),
    path('homee/', views.homee, name='homee'),
    path('index/', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('today/', views.today, name='today'),
    path('contact/', views.contact, name='contact'),
    path('logo/', views.logo, name='logo'),
    path('login/', views.login, name='account_login'),
    path('signup/', views.signup, name='account_signup'),
    path('logout/', views.logout, name='account_logout'),
    path('song/', views.song, name='song'),
    path('album/', views.album, name='album'),
    path('tablet/', views.tablet, name='tablet'),
    path('prof/', views.userProfile, name='prof'),
    path('titledeed/', views.titleDeed, name='titledeed'),
    path('deed/', views.Deed, name='deed'),
    path('add/', views.add, name='add'),
    path('addalbum/', views.addalbum, name='addalbum'),
    path('newSong/', views.newSong, name='newsong'),
    path('addsong/', views.addsong, name='addsong'),

]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)