from django.urls import path
from . import views

urlpatterns = [
    path('user_page', views.user_page, name='user_page'),
    path('donate', views.donate, name='donate'),
    path('community', views.community, name='community'),
    path('login_user', views.login_user, name='login'),
    path('logout_user', views.logout_user, name='logout'),
    path('signup_user', views.signup_user, name='signup'),
    path('settings', views.settings, name='settings'),
    ]