from django.contrib import admin
from questions.models import Article, Comment, UserProfile, Tag

# Register your models here.
admin.site.register(Article)
admin.site.register(UserProfile)
admin.site.register(Tag)
admin.site.register(Comment)
