from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.projects_view, name='projects_view'),
    path('add/', views.add_project, name='add_project'),
    path('project/<int:project_id>/update/', views.update_project, name='project_update'),
    path('project/<int:project_id>/delete/', views.delete_project, name='project_delete'),
    path('project/<int:project_id>/', views.projects_detail, name='project_detail'),
]
if settings.DEBUG:  
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
