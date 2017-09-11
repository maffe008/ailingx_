from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


class Area(models.Model):
    name = models.CharField('Area name', max_length=30)
    location = models.CharField('Area location', max_length=60)
    info = models.TextField('Area Information', max_length=500)
    sqkm = models.IntegerField('Area Square meter')

    def __unicode__(self):
        return self.name


class Block(models.Model):
    area = models.ForeignKey(Area)
    name = models.CharField('Block name', max_length=30)
    location = models.CharField('Block location', max_length=60)
    info = models.TextField('Block Information', max_length=500)
    sqkm = models.IntegerField('Block Square meter')

    def __unicode__(self):
        return self.name


class Cell(models.Model):
    block = models.ForeignKey(Block)
    user = models.ManyToManyField(User)
    name = models.CharField('Cell name', max_length=30)
    location = models.CharField('Cell location', max_length=60)
    info = models.TextField('Cell Information', max_length=500)
    sqm = models.IntegerField('Cell Square meter')
    user = models.ManyToManyField(User)

    def __unicode__(self):
        return self.name