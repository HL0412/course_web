from datetime import datetime
from django.db import models
# Create your models here.
from users.models import UserProfile




class GuestBook(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name='留言者')
    title = models.CharField(max_length=45, verbose_name='标题')
    g_content = models.TextField(verbose_name='内容')
    g_time = models.DateTimeField(default=datetime.now, verbose_name='留言时间')


    class Meta:
        db_table = 'guestbook_info'
        verbose_name = '留言管理'
        verbose_name_plural = "留言管理"

    def __str__(self):
        return self.title


class Reply(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name='回复者')
    r_content = models.TextField(verbose_name='回复内容')
    guestbook = models.ForeignKey(GuestBook, on_delete=models.CASCADE, verbose_name='留言')
    next_reply = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name='回复')
    r_time = models.DateTimeField(default=datetime.now, verbose_name='回复时间')

    class Meta:
        db_table = 'reply_info'
        verbose_name = '留言回复管理'
        verbose_name_plural = "留言回复管理"

    def __str__(self):
        return self.r_content


