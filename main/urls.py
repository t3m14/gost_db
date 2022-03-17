from django.urls import path
from .api import GostCreateApi, GostApi, GostUpdateApi, GostDeleteApi
urlpatterns = [
    path('api',GostApi.as_view()),
    path('api/create',GostCreateApi.as_view()),
    path('api/<int:pk>',GostUpdateApi.as_view()),
    path('api/<int:pk>/delete',GostDeleteApi.as_view()),
]