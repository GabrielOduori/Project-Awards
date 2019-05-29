from django.conf.urls import url
from . import views
from django.contrib.auth.views import login,logout
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    
    # url(r'^$', views.home, name='home'),
    url(r'^login/$', login, {'template_name':'accounts/login.html'}),
    url(r'^logout/$', views.logout, {"next_page": '/'}),
    
    url(r'^logout/$', logout, {'template_name': 'accounts/logout.html'}, name='logout'),
    
    
    
    url(r'^register/$',views.register, name = 'register'),
    url(r'^profile/$', views.user_profile, name = 'view_profile' ),
    url(r'^profile/edit/$', views.edit_profile, name = 'edit_profile' ),
    url(r'^change-password/$', views.change_password, name = 'change_password' )
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)