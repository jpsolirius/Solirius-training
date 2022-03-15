from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.project_index, name='project_index'),
    path('<int:pk>/', views.project_detail, name='project_detail'),
    path('new_project', views.create_project, name='new_project'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)