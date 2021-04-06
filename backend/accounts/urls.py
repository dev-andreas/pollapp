from django.urls import path, include

from . import views

urlpatterns = [

    path("password/reset/", views.CustomPasswordResetView.as_view(), name="account_reset_password"),
    path('', include('allauth.urls'))
]
