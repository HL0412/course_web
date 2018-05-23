from datetime import datetime
from django.db import models
from users.models import UserProfile
# Create your models here.


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
    r_time = models.DateTimeField(default=datetime.now, verbose_name='回复时间')
    to_user = models.ForeignKey(UserProfile, blank=True, null=True,
                                on_delete=models.CASCADE, verbose_name='二级回复者' , related_name='to_reply_user')
    # 多级回复需要进行自关联
    parent = models.ForeignKey("Reply",  on_delete=models.CASCADE, related_name="rid", null=True, blank=True)

    def __unicode__(self):
        return "{0}@{1}".format(self.user, self.to_user)

    class Meta:
        db_table = 'reply_info'
        verbose_name = '留言回复管理'
        verbose_name_plural = "留言回复管理"

