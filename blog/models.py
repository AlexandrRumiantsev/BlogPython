from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            auto_now_add=True)
    published_date = models.DateTimeField(
            blank=True, null=True,auto_now=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class UserProfile(models.Model):
    name = models.ForeignKey('auth.User')
    family = models.CharField(max_length=20)
    years = models.CharField(max_length=2)
    email = models.EmailField(max_length=20)
    skype = models.CharField(max_length=20)
    flame = models.CharField(max_length=20)
    towm = models.CharField(max_length=20)
    avatar = models.ImageField(upload_to=u'./media/img/', verbose_name=u'Аватар', blank=False)

    def create(self):
        self.save()




