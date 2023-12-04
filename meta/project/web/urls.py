from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='Home'),
    path('frontend/', views.Frontend, name='Frontend'),
    path('backend/', views.Backend, name='Backend'),
    path('contact/', views.Contact, name='Contact'),
    path('portfolio', views.Portfolio, name='Portfolio'),
    
    
    
]