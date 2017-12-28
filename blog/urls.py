from django.conf.urls import url
from . import views
from django.conf.urls import include 
urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^user/(?P<pk>\d+)/$', views.user_detail, name='user_detail'),
    url(r'^register/$', views.RegisterFormView.as_view()),
    url(r'^new/', views.newPublication, name='new'),
    url(r'^delete/(?P<pk>\d+)/$', views.delete, name='delete'),
    url(r'^edit/(?P<pk>\d+)/$', views.edit, name='edit'),
    ]
