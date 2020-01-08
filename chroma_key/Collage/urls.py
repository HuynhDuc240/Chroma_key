from django.conf.urls import url
from . import views

app_name = 'collage'

# Create url #
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name="index"),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name="detail"),
    url(r'add/$', views.CollageCreate.as_view(), name='collage-add'),
    url(r'(?P<pk>[0-9]+)/update/$', views.CollageUpdate.as_view(), name='collage-update'),
    url(r'(?P<pk>[0-9]+)/delete/$', views.CollageDelete.as_view(), name='collage-delete')
]