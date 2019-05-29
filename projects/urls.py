from django.conf.urls import url
from .import views as project_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', project_views.display_projects, name = 'index'),
    url(r'^add/$', project_views.add_project, name = 'add_project'),
    url(r'^show/$', project_views.display_projects, name = 'projects'),
    url(r'^show/(?P<id>\d+)/$', project_views.project_detail, name = 'projects-details'),


        
    
    

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

