from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
# Register your models here.
from .models import Post, CategoryOfPost, Tag


admin.site.register(Post, MarkdownxModelAdmin)
admin.site.register(CategoryOfPost)
admin.site.register(Tag)
