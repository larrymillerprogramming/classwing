from django.contrib import admin

from .models import User, Material, Post, Like, Follow

# Register your models here.
admin.site.register(User)
admin.site.register(Material)
admin.site.register(Post)
admin.site.register(Like)
admin.site.register(Follow)