from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.contrib import admin
from automobiles import views 


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^admin/$', admin.site.urls),
]