from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
                       url(r'^login/', 'loginsystem.views.login'),
                       url(r'^logout/', 'loginsystem.views.logout'),
                       )

