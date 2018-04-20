
# Register your models here.
import xadmin
from platfrom.models import News, Notice, WorkCommit


class NoticeAdmin:
    list_display = ['title', 'picture', 'publish_time']
    search_fileds = ['title']
    list_filter = ['title', 'publish_time']
    model_icon = 'fa fa-bullhorn'

class NewsAdmin:
    list_display = ['title', 'picture', 'publish_time']
    search_fileds = ['title']
    list_filter = ['title', 'publish_time']
    model_icon = 'fa fa-bullseye'

class WorkCommitAdmin:
    list_display = ['student', 'course', 'teacher', 'title', 'commit_time']
    search_fileds = ['student', 'title', 'teacher', 'course']
    list_filter = ['student', 'title']
    model_icon = 'fa fa-book'

class WorkPublishAdmin:
    list_display = ['course', 'teacher', 'title', 'publish_time']
    search_fileds = ['course', 'teacher', 'course']
    list_filter = ['course', 'teacher' ]
    model_icon = 'fa fa-edit'

xadmin.site.register(WorkCommit, WorkCommitAdmin)
xadmin.site.register(News, NewsAdmin)
xadmin.site.register(Notice, NoticeAdmin)