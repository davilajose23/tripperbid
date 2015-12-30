"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.Index),
    url(r'^login/$', views.Login),
    url(r'^signup/$', views.Registro),
    url(r'^logout/$', views.Logout),
    url(r'^trips/$', views.Trips),
    url(r'^search/$', views.Search),
    url(r'^dashboard/$', views.Dashboard),
    url(r'^dashboard/users/$', views.Dashboard_users),
    url(r'^dashboard/winners/$', views.Dashboard_winners),
    url(r'^dashboard/trips/$', views.Dashboard_trips),
    url(r'^dashboard/trips/(?P<sub_id>[0-9]+)/$', views.Dashboard_trips_details),
    url(r'^details/(?P<sub_id>[0-9]+)/$', views.Details),
    url(r'^follow/(?P<user_id>[0-9]+)/$', views.Follow),
    url(r'^settings/$', views.Settings_gen),
    url(r'^settings/profile/$', views.Settings_prof),
    url(r'^unfollow/(?P<user_id>[0-9]+)/$', views.Unfollow),
    url(r'^profile/(?P<prof_id>[0-9]+)/$', views.Profile),
    url(r'^profile/(?P<prof_id>[0-9]+)/about/$', views.Profile_about),
    url(r'^profile/(?P<prof_id>[0-9]+)/followers/$', views.Profile_followers),
    url(r'^profile/(?P<prof_id>[0-9]+)/following/$', views.Profile_following),
    url(r'^details/(?P<sub_id>[0-9]+)/p=(?P<p_id>[0-9]+)/$',views.inscribir_subasta),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
