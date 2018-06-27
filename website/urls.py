from django.conf.urls import url
from . import views
from django.urls import include, path


app_name = "website"

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^post_list/$', views.posts_list, name='posts_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^drafts/$', views.post_draft_list, name='post_draft_list'),
    url(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
    url(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),
    path('users/', include('users.urls')),
]