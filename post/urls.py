from django.urls import path
from .views import post, details

urlpatterns = [
    path('', post, name='post'),
    path('content/<int:pk>', details, name='contents')
]
