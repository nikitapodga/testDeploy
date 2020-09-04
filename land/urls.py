from django.urls import path
from django.conf.urls import url
from . import views
from django.views.generic.base import RedirectView

urlpatterns = [
    # url(r'^$', RedirectView.as_view(url='land/')),
	# url(r'^blog/$', RedirectView.as_view(url='/posts/')), #2
	# url(r'^google/$', RedirectView.as_view(url='http://google.com')), #3
    path('', views.index, name='index'),
    path('men/', views.men, name='men'),
    path('single/', views.single, name='single'),
    path('women/', views.women, name='women'),
    path('error404/', views.error404, name='404'),
    path('about/', views.about, name='about'),
    path('add-to-cart/', views.addtocart, name='add-to-cart'),
    path('registration/login/', views.reglogin, name='login'),
    path('registration/logout/', views.reglogout, name='logout'),
]