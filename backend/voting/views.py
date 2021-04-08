from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views import View

# Create your views here.

from .decorators import user_authenticated, user_unauthenticated


@user_unauthenticated
def index(request):
    return render(request, 'index.html', {})

@user_authenticated
def test(request):
    return render(request, 'account/verification_sent.html', {})


@method_decorator(user_authenticated, name='dispatch')
class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'user.html', self.get_context_data(*args, **kwargs))

    def get_context_data(self, *args, **kwargs):
        return {}
