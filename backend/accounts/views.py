from django.shortcuts import render
from django.utils.decorators import method_decorator

from allauth.account.views import PasswordResetView

# Create your views here.

from user.decorators import user_unauthenticated

@method_decorator(user_unauthenticated, name='dispatch')
class CustomPasswordResetView(PasswordResetView):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

