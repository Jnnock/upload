from django.conf.urls import patterns, url
from up import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    #url(r'^upload/$',views.upload,name='upload'),
    url(r'^list/$',views.list,name='list'),
    url(r'^search/$',views.search,name='search'),
    #url(r'^result/$',views.action,name='action'),
    url( r'^css/(?P<path>.*)$', 'django.views.static.serve', 
        { 'document_root': '/Users/apple/Documents/upload/templates/public/css' } 
	),
	url( r'^js/(?P<path>.*)$', 'django.views.static.serve', 
        { 'document_root': '/Users/apple/Documents/upload/templates/public/js' } 
    ), 
    url( r'^fonts/(?P<path>.*)$', 'django.views.static.serve', 
        { 'document_root': '/Users/apple/Documents/upload/templates/public/fonts' } 
    ),
    url( r'^files/(?P<path>.*)$', 'django.views.static.serve', 
        { 'document_root': '/Users/apple/Documents/upload/templates/files' } 
	), 
)
