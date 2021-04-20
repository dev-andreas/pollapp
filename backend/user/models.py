from django.db import models
from django.db.models.signals import post_save
from django.core.exceptions import ValidationError

# Create your models here.

from accounts.models import User
from django.utils import timezone

class Poll(models.Model):
    title = models.CharField(max_length=256)
    description = models.CharField(max_length=1024)
    votes_amt = models.PositiveSmallIntegerField(default=1)
    less_allowed = models.BooleanField(default=False)
    show_while_running = models.BooleanField(default=False)

    date_created = models.DateTimeField(auto_now=True)
    date_to_start = models.DateTimeField(null=True)
    date_to_end = models.DateTimeField(null=True)

    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')
    voters = models.ManyToManyField(User, through='Voter', related_name='voters')

    id_hashed = models.CharField(max_length=32, null=True)

    @classmethod
    def post_create(cls, sender, instance, created, *args, **kwargs):
        if not created:
            return
        
        # Creating poll identification "hash"
        # Made out of creation year, month and poll id % 9999 (I don't think more than 1,000,000 polls will be created per month...)
        # Then everything will be encoded to hexadecimal

        id_hashed = hex(int('{id}{year}{month}'.format(
            year=instance.date_created.year, 
            month=instance.date_created.month, 
            id=instance.id % 999999,
        )))[2:]

        instance.id_hashed = id_hashed
        instance.save()

post_save.connect(Poll.post_create, sender=Poll)


class Choice(models.Model):
    name = models.CharField(max_length=256)
    votes = models.IntegerField(default=0)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)


class Voter(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)