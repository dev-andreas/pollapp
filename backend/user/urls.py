from django.urls import path, include
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^home.*$', views.UserView.as_view(), name='user'),

    # apis
    path('api/user/', views.UserAPI.as_view(), name='user_data'),
    path('api/create_poll/', views.CreatePollAPI.as_view(), name="create_poll")
]