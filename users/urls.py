from django.urls import path
from .views import admin, profile, RegisterView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin, name='admin'),
    path('register/', RegisterView.as_view(), name='users-register'),
    path('profile/', profile, name='users-profile'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    
]
