from django.urls import path
from . import views

app_name = 'feedback'
urlpatterns = [
    path('', views.get_feedback, name='get_feedback'),
]
