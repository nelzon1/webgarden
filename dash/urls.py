from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='dash-home'),
    path('test', views.test, name='dash-test'),
    path('update', views.update, name='dash-update'),
]