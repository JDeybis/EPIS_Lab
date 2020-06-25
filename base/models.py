from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None, is_active=True, is_staff=False, is_admin=False):
        if not username:
            raise ValueError("User must have an username.")
        if not password:
            raise ValueError("User must have an password.")

        user_obj = self.model(
            username=username,
            email=self.normalize_email(email)
        )

        user_obj.set_password(password)
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.active = is_active
        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self, username, email, password=None):
        user = self.create_user(
            username,
            email=email,
            password=password,
            is_staff=True,
        )

        return user

    def create_superuser(self, username, email, password=None):
        user = self.create_user(
            username,
            email=email,
            password=password,
            is_staff=True,
            is_admin=True
        )

        return user


class User(AbstractBaseUser):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    student_code = models.CharField(max_length=8, blank=True, null=True)
    student = models.BooleanField(default=True)
    is_enrollment = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    def __str__(self):
        return self.username

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active
