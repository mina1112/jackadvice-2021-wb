from django.db import models

# Create your models here.
import datetime
from django.db.models.fields import CharField, IntegerField
from django.utils import timezone
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import gettext_lazy as _
from pytz import timezone
import uuid



class User(AbstractBaseUser, PermissionsMixin):
    username_validator = UnicodeUsernameValidator()
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    username = models.CharField(
        _("username"),
        max_length=150,
        unique=True,
        null = True,
        help_text=_("Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."),
        validators=[username_validator],
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )
    
    line_id = models.CharField(
        _("userId"),
        max_length=100,
        unique=True,
    )

    include_default_voice = models.BooleanField("デフォルトボイス含むかどうか", default=True)
    email = models.EmailField("メールアドレス", blank=True, unique=True)
    is_staff = models.BooleanField("is_staff", default=False)
    is_active = models.BooleanField("is_active", default=True)

    objects = UserManager()

    USERNAME_FIELD = "username"
    EMAIL_FIELD = "username"
    REQUIRED_FIELDS = ["email"]
    
    def __str__(self):
        return self.username


class Voices(models.Model):
    title = models.CharField(help_text='曲名', max_length=30)
    id = id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    file_path = models.CharField(max_length=100)
    is_default = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title

class Tasks(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(User, to_field='id', on_delete=models.CASCADE)
    title = models.CharField(max_length=100, help_text='タスクの名前')
    deadline = models.DateTimeField(help_text='締め切り')
    target_datetime = models.DateTimeField(help_text='目標日')
    notificate_at = models.DateTimeField(help_text='通知日')
    memo = models.CharField(max_length=100, help_text='タスクの詳細')
    is_closed = models.BooleanField(default=False, help_text='終わったかどうか')
    voice = models.ForeignKey(Voices, on_delete=models.CASCADE, default="")
    def __str__(self):
        return self.title




