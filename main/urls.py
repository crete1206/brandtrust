from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('service/', views.service, name='service'),
    path('event/', views.event, name='event'),
    path('blog/', views.blog, name='blog'),
    path('book/', views.book, name='book'),
    path('menu/', views.menu, name='menu'),
    path('team/', views.team, name='team'),
    path('testimonial/', views.testimonial, name='testimonial'),
    path('404/', views.error_404, name='error_404'),
]