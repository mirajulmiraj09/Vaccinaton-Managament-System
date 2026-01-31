from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from django.conf import settings
from accounts.managers import MyUserManager


class Role(models.Model):
    role_name = models.CharField(max_length=50,unique=True)
    permissions = models.JSONField(null=True,blank=True)

    def __str__(self):
        return self.role_name
    
class User(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(max_length=255,unique=True,db_index=True)
    password = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    roles = models.ManyToManyField(Role,through='UserRole')

    objects = MyUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
    

class UserRole(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    assigned_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'role')


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        unique=True
    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    nid = models.CharField(max_length=20, unique=True, db_index=True)
    dob = models.DateField()
    gender = models.CharField(max_length=10, null=True, blank=True)
    phone = models.CharField(max_length=20)
    address = models.TextField()
    specialization = models.CharField(max_length=100, null=True, blank=True)
    medical_history = models.TextField(null=True, blank=True)
    profile_pic_url = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
