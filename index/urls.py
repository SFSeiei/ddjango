from django.urls import path
from . import views

app_name = 'index'
urlpatterns = [
    path('', views.img),
    path('index1', views.xyz, name='login1'),
    path('file/', views.get_file),
    path('set_cookie/', views.set_cookie),
    path('get_cookie/', views.get_cookie),
    path('add_user', views.add_user),
    path('url_param/<id>', views.url_param, name="url_param"),
    path('request_param/', views.request_param, name="request_param"),
]
