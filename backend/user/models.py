from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.

from accounts.models import User

class Poll(models.Model):
    title = models.CharField(max_length=256)
    description = models.CharField(max_length=1024)
    votes_amt = models.PositiveSmallIntegerField(default=1)
    less_allowed = models.BooleanField(default=False)
    show_while_running = models.BooleanField(default=False)

    date_created = models.DateTimeField(auto_now=True)
    date_to_start = models.DateTimeField(null=True)
    date_to_end = models.DateTimeField(null=True)

    owner = models.OneToOneField(User, on_delete=models.CASCADE, related_name='owner')
    voters = models.ManyToManyField(User, through='Voter', related_name='voters')

class Choice(models.Model):
    name = models.CharField(max_length=256)
    votes = models.IntegerField(default=0)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)

class Voter(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)