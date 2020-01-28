from django.urls import path
from . import views

app_name = 'recargacoin'
urlpatterns = [
    path('', views.run, name='run'),
]
