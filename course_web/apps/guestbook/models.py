from datetime import datetime
from django.db import models
# Create your models here.
from users.models import UserProfile


class GuestBook(models.Model):
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name='留言者')
    title = models.CharField(max_length=45, verbose_name='标题')
    g_content = models.TextField(verbose_name='内容')
    g_time = models.DateTimeField(default=datetime.now, verbose_name='留言时间')
    ID_Card = models.CharField(max_length=50, default=0, verbose_name='留言ID')
    checkout = models.BooleanField(default=False, verbose_name='是否通过审核')
    r_content = models.TextField(verbose_name='回复内容')
    r_time = models.DateTimeField(default=datetime.now, verbose_name='回复时间')
    type = models.IntegerField(choices=((1, '发表'), (2, '回复')), default=1, verbose_name='类型')

    class Meta:
        db_table = 'guestbook_info'
        verbose_name = '留言管理'
        verbose_name_plural = "留言管理"

    def __str__(self):
        return self.author

