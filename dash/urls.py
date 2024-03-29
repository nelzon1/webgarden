from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='dash-home'),
    path('test', views.test, name='dash-test'),
    path('update', views.update, name='dash-update'),
    path('getImage', views.getImage,name='dash-getImage'),
    path('fetchImage/<str:filename>', views.fetchImage,name='dash-fetchImage'),
    path('heartbeat/<int:time>', views.heartbeat,name='dash-heartbeat')
]