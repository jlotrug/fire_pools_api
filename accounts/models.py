from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class CustomUserManager(BaseUserManager):

    def creat_user(self, password, username):
        if not username:
            raise ValueError("User must provide username")
        
        user = self.model(username=username)
        user.set_password(password)
        user.save()

        return user
    


class CustomUserModel(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    
    def __str__(self):
        return self.username
