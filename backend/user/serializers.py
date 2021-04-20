from rest_framework.serializers import ModelSerializer, Serializer
from rest_framework import serializers

from accounts.models import User

from .models import Poll, Choice
from django.utils import timezone


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name',
                  'last_name', 'email', 'date_joined']
        read_only_fields = ['date_joined']

class PollReprSerializer(ModelSerializer):
    class Meta:
        model = Poll
        fields = ['title', 'id_hashed', ]

class PollSerializer(ModelSerializer):

    choices = serializers.ListField()

    class Meta:
        model = Poll
        fields = '__all__'
        read_only_fields = ['date_created', 'owner', 'voters', 'id_hashed']
        extra_kwargs = {
            "title": {"error_messages": {"blank": "Title must not be empty!"}},
            "description": {"error_messages": {"blank": "Description must not be empty!"}},
            "date_to_start": {"error_messages": {"invalid": "Starting date must not be empty!"}},
            "date_to_end": {"error_messages": {"invalid": "Ending date must not be empty!"}},
        }

    def __init__(self, instance=None, data=None, user=None, **kwargs):
        self.user = user
        super().__init__(instance=instance, data=data, **kwargs)

    def validate(self, attrs):
        if attrs['title'].isspace():
            raise serializers.ValidationError(
                'Title must contain at least one none-whitespace character!')
        if attrs['description'].isspace():
            raise serializers.ValidationError(
                'Description must contain at least one none-whitespace character!')
        if attrs['votes_amt'] < 1:
            raise serializers.ValidationError(
                'Votes amount must be higher than 0!')
        if attrs['date_to_start'] >= attrs['date_to_end']:
            raise serializers.ValidationError(
                'Ending date must occur after starting date!')
        if attrs['less_allowed'] and attrs['votes_amt'] == 1:
            raise serializers.ValidationError(
                'Less votes are only allowed if votes amount per user is higher than one!')
        if len(attrs['choices']) < 2:
            raise serializers.ValidationError(
                'There must be at least two choices!')
        if attrs['votes_amt'] > len(attrs['choices']):
            raise serializers.ValidationError(
                'Votes amount per user must not be higher than the amount of choices!')

        # check if date_to_start and date_to_end is not in the past
        return super().validate(attrs)

    def create(self, validated_data):
        poll = Poll(
            title=validated_data['title'],
            description=validated_data['description'],
            votes_amt=validated_data['votes_amt'],
            less_allowed=validated_data['less_allowed'],
            show_while_running=validated_data['show_while_running'],
            date_to_start=validated_data['date_to_start'],
            date_to_end=validated_data['date_to_end'],
            owner=self.user,
        )

        poll.save()

        for item in self.validated_data['choices']:
            choice = Choice(name=item, poll=poll)
            choice.save()

        return poll

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
        

class ChoiceSerializer(ModelSerializer):
    class Meta:
        model = Choice
        fields = '__all__'
        read_only_fields = ['name', 'poll']