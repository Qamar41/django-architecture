from django.contrib import admin
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest')),
    path('api-token-auth', obtain_jwt_token),
    path('users/', include(('app_dir.user.urls', 'user'), namespace='user')),
    path('api/users/', include(('app_dir.user.api.urls', 'user_api'), namespace='user_api')),
]

