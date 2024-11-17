from django.urls import path
from . import views


urlpatterns = [
    path('', views.blog_view, name='blog'),
    path('add/', views.add_post, name='add_post'),
    path('<int:blog_id>/', views.posts_detail, name='posts_detail'),
    path('<int:blog_id>/update/', views.update_post, name='posts_update'),
    path('delete/<int:blog_id>/', views.delete_post, name='posts_delete'),
    path('delete_comment/<int:comment_id>/', views.delete_comment, name='comments_delete'),
]
