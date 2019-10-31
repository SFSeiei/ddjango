from django.urls import path
from . import views
# from django.conf.urls import url, include
# from django.contrib.auth.models import User
# from rest_framework import serializers, viewsets, routers
#
app_name = 'login'
#
# # Serializers define the API representation.
# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ['url', 'username', 'email', 'is_staff']
#
#
# # ViewSets define the view behavior.
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#
# # Routers provide a way of automatically determining the URL conf.
# router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)

urlpatterns = [
    path('', views.abc),
    path('login1', views.cde, name='login1'),
    path('sqlite/<nid>', views.opertation),
    path('get_user_connection', views.get_user_connection),
    path('add_user', views.add_user),
    path('get_all_user', views.get_all_user),
    path('get_user', views.ger_user),
    path('q_get_user', views.q_get_user),
    path('delete_user', views.delete_user),
    path('update_user', views.update_user),
    path('get_sql', views.get_sql),
    path('aggregate',views.aggregate),
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
