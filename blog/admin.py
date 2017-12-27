# import self as self
from django.contrib import admin
from .models import Post
from django import forms
from .models import UserProfile
from django.contrib.auth.admin import UserAdmin

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ['created_date', 'published_date']
admin.site.register(Post, PostAdmin)

#/////////////////////////////////

class MyUserAdmin(UserAdmin):
    #form = UserChangeForm
    #add_form = UserCreationForm
    list_display = ('email', 'password', 'name', 'surname', 'phone',
                    'skype', 'img_avatar', 'is_admin', 'is_active',)
    list_filter = ('email',)
    fieldsets = (
    (None, {'fields': ('email', 'password')}),
    ('Personal info', {'fields': ('name', 'surname', 'phone', 'skype', 'avatar', )}),
    ('Permissions', {'fields': ('is_admin', 'is_active')}),
    )
    add_fieldsets = (
    (None, {
    'classes': ('wide',),
    'fields': ('email', 'password1', 'password2')}
    ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()



admin.site.register(UserProfile)










