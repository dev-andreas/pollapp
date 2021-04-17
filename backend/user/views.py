from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views import View
from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import APIView

# Create your views here.

from .decorators import user_authenticated, user_unauthenticated
from .serializers import UserSerializer, PollSerializer
from .validators import PollValidator
from .models import Poll

@user_unauthenticated
def index(request):
    return render(request, 'index.html', {})


@method_decorator(user_authenticated, name='dispatch')
class UserView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'user.html', self.get_context_data(*args, **kwargs))

    def get_context_data(self, *args, **kwargs):
        return {
            'user': UserSerializer(self.request.user).data,
        }


@method_decorator(user_authenticated, name='dispatch')
class UserAPI(APIView):
    def get(self, request, *args, **kwargs):
        return JsonResponse(UserSerializer(self.request.user).data)

    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(self.request.user, data=request.POST)
        if serializer.is_valid():
            user = serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@method_decorator(user_authenticated, name='dispatch')
class CreatePollAPI(APIView):
    def post(self, request, *args, **kwargs):

        serializer = PollSerializer(data=self.request.POST, user=request.user)

        if serializer.is_valid():
            poll = serializer.save()
            return JsonResponse({'data': request.POST}, status=status.HTTP_200_OK)
        else:
            return JsonResponse(serializer.errors, status= status.HTTP_400_BAD_REQUEST)