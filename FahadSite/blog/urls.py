from django.urls import path
from . import views


urlpatterns = [
    path('', views.blog_view, name='blog'),
    path('add/', views.add_post, name='add_post'),
    path('<int:blog_id>/', views.blog_detail_view, name='blog_detail'),
    path('<int:blog_id>/update/', views.update_post, name='update_post'),
    path('delete/<int:blog_id>/', views.delete_post, name='delete_post'),
    path('delete_comment/<int:comment_id>/', views.delete_comment, name='delete_comment'),
]
