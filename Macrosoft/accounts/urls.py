from django.conf.urls import url
from . import views
from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^$', views.home),
    url(r'^login/$', login, {'template_name': 'accounts/login.html'}),
    url(r'^logout/$', logout, {'template_name': 'accounts/logout.html'}),
    url(r'^register/$', views.register, name='register'),
    url(r'^profile/$', views.view_profile, name='view_profile'),
    url(r"application_submit/$", views.submit_app, name = "app_submit"),
    url(r'^profile/edit_profile/$', views.edit_profile, name='edit_profile'),
    url(r'app_detail/', views.app_page, name="apppage"),
    url(r'search/', views.search_page, name = "search_app" ),

]