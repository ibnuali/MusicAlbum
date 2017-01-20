from django.conf.urls import url
from . import views

app_name = 'music'

urlpatterns = [
    #index music
    url(r'^$',views.indexView.as_view(),name='index'),
    #music by id
    url(r'^(?P<pk>[0-9]+)/$', views.detailView.as_view(), name='detail'),
    url(r'hello/$', views.hello.as_view(), name='hello'),
    #add album
    url(r'^album/add/$', views.albumCreate.as_view() , name='Album-add'),
    url(r'album/(?P<pk>[0-9]+)/$', views.albumUpdate.as_view() , name='Album-update'),
    url(r'album/(?P<pk>[0-9]+)/delete/$', views.albumDelete.as_view() , name='Album-delete'),
]

#old
"""
    urlpatterns = [
        #index music
        url(r'^$',views.index,name='index'),
        #music by id
        url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),
        #music by id / favorite
        url(r'^(?P<album_id>[0-9]+)/favorite$', views.favorite, name='favorite'),
    ]
"""
