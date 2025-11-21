from django.db import models


class User(models.Model):
    username = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=128)
    email = models.EmailField(unique=True, blank=True, null=True)
    phone = models.CharField(max_length=13, blank=True, null=True)
    
    def __str__(self):
        return self.username
    
    
class Profile(models.Model):
    first_name = models.CharField(max_length=128, blank=True, null=True)
    last_name = models.CharField(max_length=128, blank=True, null=True)
    bio = models.CharField(max_length=256, blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', default='avatars/default.png')
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    def __str__(self):
        return self.user.username
    