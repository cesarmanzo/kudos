from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Organization(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=200, blank=False, unique=True)
    logo = models.ImageField(blank=True, upload_to='logos', height_field=None, width_field=None, max_length=200)

    def __str__(self):
        return self.name


class Kudo(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    sent_by = models.ForeignKey(User, related_name='sent_by', on_delete=models.CASCADE)
    sent_to = models.ForeignKey(User, related_name='sent_to', on_delete=models.CASCADE)
    message = models.TextField(blank = True)

    def __int__(self):
        return self.id


class UserData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    kudos_available = models.PositiveSmallIntegerField(default=3)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name
