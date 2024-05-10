from django.urls import path, include
from . import views

urlpatterns = [
    path('get_post/', views.get_post, name='get_post'),
    path('set_post/', views.set_post, name='set_post')
]