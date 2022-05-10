from django.db import models
from django.contrib.auth.models import User


class Organization(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=200, blank=False, unique=True)
    logo = models.ImageField(blank=True, upload_to='logos', height_field=None, width_field=None, max_length=200)


class Kudo(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    sent_by = models.ForeignKey(User, related_name='sent_by', on_delete=models.CASCADE)
    sent_to = models.ForeignKey(User, related_name='sent_to', on_delete=models.CASCADE)
    message = models.TextField(blank = True)


class UserData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    kudos_available = models.IntegerField()
