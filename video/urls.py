from django.conf.urls import include,url
from . import views

urlpatterns = [
        url(r'^$', views.video_list),
	url(r'^video/(?P<pk>[0-9]+)/$',views.video_detail),
    ]
