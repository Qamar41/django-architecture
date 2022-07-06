from django.urls import path

from .views import (
    UserListAPIView, UserCreateAPIView,
)


urlpatterns = [
    path('', UserListAPIView.as_view(), name='user-list'),
    path('create', UserCreateAPIView.as_view(), name='user-creator'),
]
