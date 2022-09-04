from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """ユーザ"""

    class UserType(models.TextChoices):
        """ユーザー区分"""
        GENERAL = 'GENERAL', '一般'
        ADMIN = 'ADMIN', '管理者'

    class Meta(AbstractUser.Meta):
        db_table = 'custom_user'

    email = models.EmailField("メールアドレス", max_length=255, unique=True)
    user_type = models.CharField(max_length=10, choices=UserType.choices)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
