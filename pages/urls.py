from django.urls import path
from pages import views


urlpatterns = [
    path('', views.index, name='index'),
    path('services', views.services, name='services'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
    path('register', views.register, name='register'),
    path('signin', views.signin, name='signin'),
    path('customer/<int:id>', views.customer, name='customer'),
    path('add', views.add, name='add'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('remove/<int:id>', views.remove, name='remove'),
]