from django.conf.urls import url
from home import views as home_views
from projects import views as project_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', home_views.home, name = 'home-page'),
    url(r'^api/profile/$', project_views.ProfileAPI.as_view()),
    url(r'^api/project/$', project_views.ProjectAPI.as_view()),
      
    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

