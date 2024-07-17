from django.urls import path
from .views import index, post_picture, post_detail, add_comment

urlpatterns = [
    path('', index, name='index'),
    path('post_picture/', post_picture, name='post_picture'),
    path('post_detail/<int:pk>/', post_detail, name='post_detail'),
    path('add_comment/<int:post_id>/', add_comment, name='add_comment'),
]
