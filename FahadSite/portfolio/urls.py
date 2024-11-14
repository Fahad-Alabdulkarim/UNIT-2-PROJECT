from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.projects_view, name='projects_view'),
    path('add/', views.add_project, name='add_project'),
    path('project/<int:project_id>/update/', views.update_project, name='update_project'),
    path('project/<int:project_id>/delete/', views.delete_project, name='delete_project'),
    path('project/<int:project_id>/', views.project_details, name='project_details'),
]
if settings.DEBUG:  
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
