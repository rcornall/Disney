from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),

    # /movies/<TITLE>/
    url(r'^(?P<_title>[\w., ]+)/$', views.movie, name='movie'),
]
