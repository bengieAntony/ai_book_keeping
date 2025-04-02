from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home'),
    path('receive-text/', views.receive_text, name='receive_text'),
]
