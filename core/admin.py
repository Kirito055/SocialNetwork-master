from django.contrib import admin
from .models import Profile,Following,Follower,Post,Comment,Message,Chat

class ProfileRegister(admin.ModelAdmin):
    fields = ('user', 'profile_photo', 'status_info')
    list_display = ('user', 'profile_photo', 'status_info')
    list_filter = ['user']
    search_fields = ['user']


admin.site.register(Profile, ProfileRegister)
admin.site.register(Follower)
admin.site.register(Following)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Chat)
admin.site.register(Message)

