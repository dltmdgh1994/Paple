from django.contrib import admin
from bbs.models import User, Group, Post, Question, Comment


admin.site.register(User)
admin.site.register(Group)
admin.site.register(Post)
admin.site.register(Question)
admin.site.register(Comment)