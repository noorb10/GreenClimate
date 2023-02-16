from django.urls import path
from . import views

urlpatterns = [
    path('login_user', views.login_user, name='login'),
    path('logout_user', views.logout_user, name='logout'),
    path('signup_user', views.signup_user, name='signup'),
    path('settings', views.settings, name='settings'),
    ]