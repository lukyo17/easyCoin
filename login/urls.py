from django.urls import path
from . import views

app_name = 'login'
urlpatterns = [
     path('', views.get_login, name='get_login'),
     path('auth_logout', views.auth_logout, name='auth_logout')
]
