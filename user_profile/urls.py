from django.urls import path
from . import views

# Urls
urlpatterns = [
    path('profile/', views.profile, name='profile'),
]
