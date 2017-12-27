# import self as self
from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    readonly_fields = ['created_date', 'published_date']
admin.site.register(Post, PostAdmin)

#/////////////////////////////////









