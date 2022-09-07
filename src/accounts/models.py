from __future__ import unicode_literals


from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.


class city(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class profile(models.Model):
    user = models.OneToOneField(
        User, related_name='user', on_delete=models.CASCADE)
    city = models.ForeignKey(city, related_name='city',
                             on_delete=models.CASCADE, blank=True, null=True)
    phone = models.CharField(max_length=50)
    image = models.ImageField(upload_to="profile/", blank=True, null=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        profile.objects.create(user=instance)

    # instance.profile.save()
