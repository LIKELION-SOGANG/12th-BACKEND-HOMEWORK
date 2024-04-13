from django.urls import path
from .views import post_list, create_post, user_list

urlpatterns = [
    path("user_list/", user_list, name="user_list"),
    path("post_list/", post_list, name="post_list"),
    path("post/<int:user_id>/", create_post, name="create_post"),
]