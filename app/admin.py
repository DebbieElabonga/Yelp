from django.contrib import admin
from .models import Post, Profile, Review, Follow

# Register your models here.
admin.site.register(Post)
admin.site.register(Profile)
admin.site.register(Review)
admin.site.register(Follow)