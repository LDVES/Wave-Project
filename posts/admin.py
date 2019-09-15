from django.contrib import admin
from posts.models import Post
from django.contrib.auth.models import Group, User

admin.site_header = 'Tytuł'

admin.site.register(Post)
admin.site.unregister(Group)
admin.site.unregister(User)



# Register your models here.
