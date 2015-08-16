__author__ = 'josegregorio'

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login$', views.LoginView.as_view(), name='login'), #
    url(r'^register', views.RegisterView.as_view(), name='register'),
    url(r'^logout', views.LogoutView.as_view(), name='logout'),
    url(r'^reset_password', views.password_reset, name='password_reset'),
]