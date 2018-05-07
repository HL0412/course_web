from datetime import datetime

from django.db import models

# Create your models here.
class GuestBook(models.Model):
    author = models.CharField(max_length=45, null=True, verbose_name='留言者')
    title = models.CharField(max_length=45, verbose_name='标题')
    g_content = models.TextField(verbose_name='内容')
    g_time = models.DateTimeField(default=datetime.now, verbose_name='留言时间')
    sex = models.CharField(max_length=6, choices=(('男', '男'), ('女', '女')), default='女', verbose_name='性别')
    ID_Card = models.CharField(max_length=50, default=0, verbose_name='留言ID')
    checkout = models.BooleanField(default=False, verbose_name='是否通过审核')
    r_content = models.TextField(verbose_name='回复内容')
    r_time = models.DateTimeField(default=datetime.now, verbose_name='回复时间')
    type = models.IntegerField(choices=((1, '发表'), (2, '回复')), default=1, verbose_name='类型')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')      #指的是后台插入内容的时间

    class Meta:
        db_table = 'guestbook_info'
        verbose_name = '留言管理'
        verbose_name_plural = "留言管理"

    def __str__(self):
        return self.author

