from django.urls import path, include
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^user/.*$', views.HomeView.as_view(), name='home'),
]