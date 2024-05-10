from django.urls import path, include
from . import views

urlpatterns = [
    path('post_list/', views.post_list, name='post_list'),
    path('user_list/', views.user_list, name='user_list'),
    # path('post/<int:pk>', views.post, name='post')
]