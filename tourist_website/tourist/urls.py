from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('destination/', views.destination_detail, name='destination'),
    path('signup/', views.signup, name="signup"),
    path('login/', views.login, name="login"),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('icons/', views.icons_view, name='icons_view'),
    path('register-booking/', views.register_booking, name='register_booking'),
]
