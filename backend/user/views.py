from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views import View
from django.http import JsonResponse
from django.utils import timezone
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.

from .decorators import user_authenticated, user_unauthenticated
from .serializers import UserSerializer, PollSerializer, PollCreationSerializer, ChoiceSerializer, PollRunningChoiceSerializer, VotingSerializer
from .validators import PollValidator
from .models import Poll, Choice


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
        print(request.POST)
        serializer = UserSerializer(self.request.user, data=request.POST)
        if serializer.is_valid():
            user = serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@method_decorator(user_authenticated, name='dispatch')
class CreatePollAPI(APIView):
    def post(self, request, *args, **kwargs):

        serializer = PollCreationSerializer(
            data=self.request.POST, user=request.user)

        if serializer.is_valid():
            poll = serializer.save()
            return Response('Poll successfully created.', status=status.HTTP_200_OK)
        else:
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@method_decorator(user_authenticated, name='dispatch')
class PollAPI(APIView):

    def dispatch(self, request, *args, **kwargs):
        self.poll = Poll.objects.filter(id_hashed=kwargs['id_hashed'])
        if self.poll.exists():
            self.poll = self.poll[0]
        else:
            return Response('Poll not existing.', status=status.HTTP_404_NOT_FOUND)
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        choices = None

        if self.poll.show_while_running or (not self.poll.show_while_running and self.poll.date_to_end <= timezone.now()):
            choices = ChoiceSerializer(
                self.poll.choice_set.all(), many=True).data
        else:
            choices = PollRunningChoiceSerializer(
                self.poll.choice_set.all(), many=True).data

        return JsonResponse({
            'poll': PollSerializer(self.poll).data,
            'choices': choices,
            'poll_owner': UserSerializer(self.poll.owner).data,
            'user_is_owner': self.poll.owner.id == request.user.id,
        })


    def post(self, request, *args, **kwargs):
        if not self.poll.owner.id == self.request.user.id:
            return Response('You are not permitted to change this poll!', status=status.HTTP_401_UNAUTHORIZED)

        serializer = PollSerializer(self.poll, data=request.POST)

        if serializer.is_valid():
            serializer.save()
            return Response('Poll successfully changed!', status=status.HTTP_200_OK)
        else:
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        if not self.poll.owner.id == self.request.user.id:
            return Response('You are not permitted to delete this poll!', status=status.HTTP_401_UNAUTHORIZED)

        self.poll.delete()

        return Response('Poll successfully deleted!', status=status.HTTP_200_OK)


@method_decorator(user_authenticated, name='dispatch')
class PollReprAPI(APIView):
    def get(self, request, *args, **kwargs):
        polls_created = Poll.objects.filter(owner=self.request.user.id)
        polls_voted = self.request.user.voters.all()

        return JsonResponse({
            'polls_created': PollSerializer(polls_created, many=True, context={
                'fields': {'title', 'id_hashed'}
            }).data,
            'polls_voted': PollSerializer(polls_voted, many=True, context={
                'fields': {'title', 'id_hashed'}
            }).data,
        })


@method_decorator(user_authenticated, name='dispatch')
class SubmitVoteAPI(APIView):
    def post(self, request, *args, **kwargs):
        user = request.user
        poll = Poll.objects.filter(id_hashed=kwargs['id_hashed'])

        # check if poll exists
        if poll.exists():
            poll = poll[0]
        else:
            return Response('Poll not existing.', status=status.HTTP_404_NOT_FOUND)

        # validate vote
        serializer = VotingSerializer(
            data=request.POST, poll=poll, user=request.user)

        if serializer.is_valid():
            serializer.save()
            return Response('Vote successfully submitted!', status=status.HTTP_200_OK)
        else:
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
