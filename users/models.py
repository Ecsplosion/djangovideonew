from django.db import models
import uuid
from django.contrib.auth.models import User
from django.db.models.signals import post_save
import os
from django.core.exceptions import ValidationError
# Create your models here.
def validate_file_extension(value):
    if value.file.content_type != 'video/mp4':
        raise ValidationError(u'Error message')
class Video(models.Model):
    video = models.FileField(validators=[validate_file_extension])
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200, null=True,blank=False)
    likes = models.ManyToManyField(User, related_name="video_likes")
    dislikes = models.ManyToManyField(User, related_name="video_dislikes")
    description = models.TextField(max_length=500, null=True, blank=True)
    id  = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    def __str__(self):
        return self.title
class UserProfile(models.Model):
    name = models.CharField(max_length=100, null=True, blank=False)
    user= models.OneToOneField(User, on_delete=models.CASCADE)
    subscriptions = models.ManyToManyField("UserProfile",  blank=True)
    profile_created = models.DateField(auto_now_add=True)
    channel_logo = models.ImageField(null=True, blank=True)
    def __str__(self):
        return self.name
def createProfile(sender,instance,created, **kwargs):
    if created:
        user= instance
        profile = UserProfile.objects.create(
            name = user.first_name +" "+ user.last_name,
            user = user,
        )
post_save.connect(createProfile, sender=User)