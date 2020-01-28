from django.urls import path
from . import views

app_name = 'relatorio'
urlpatterns = [
    path('', views.get_relatorio, name='get_relatorio'),
]
