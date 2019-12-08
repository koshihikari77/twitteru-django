from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Tweet, UserProfile, Image
# Register your models here.

"""
class PostInline(admin.TabularInline):
    model = Post
    extra = 3


class CustomUserAdmin(UserAdmin):
    inlines = [PostInline]
"""


admin.site.register(Tweet)
admin.site.register(UserProfile)

admin.site.register(Image)
