from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager
)
from django.core.validators import RegexValidator


class UserManager(BaseUserManager):
    def create_user(self, phone_number, password=None, is_active=True, is_staff=False, is_admin=False):
        if not phone_number:
            raise ValueError("Users must have a phone number")
        if not password:
            raise ValueError("Users must have a password")
        user = self.model(phone_number=phone_number)
        user.set_password(password)
        user.active = is_active
        user.staff = is_staff
        user.admin = is_admin
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password=None):
        user = self.create_user(
            phone_number=phone_number,
            password=password,
            is_admin=True,
            is_staff=True
        )
        return user


class User(AbstractBaseUser):
    phone_number = models.CharField(
        unique=True,
        max_length=10,
        validators=[RegexValidator(r'^\d{10}$')]
    )
    active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    admin = models.BooleanField(default=False)
    staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'phone_number'

    objects = UserManager()

    def __str__(self):
        return str(self.phone_number)

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
