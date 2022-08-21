from django.db import models


class BaseModel(models.Model):
    """ベースモデル"""

    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)

    class Meta:
        # マイグレーションしてもテーブルを作らないように
        abstract = True
