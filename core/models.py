from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_photo = models.FileField(default='default.jpg', upload_to='profile_photos')
    status_info = models.CharField(default="Enter status", max_length=1000)

    def __str__(self):
        return f'{self.user.username} Profile'


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    post_text = models.CharField(max_length=2000)
    post_picture = models.FileField(default="default.jpg", upload_to='post_picture')
    rating=models.FloatField(default=0.0)
    def get_rating(self):
        return self.rating

class Following(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    following_user = models.CharField(max_length=100, null=True)

    # def __str__(self):
    #     return self.following_user.username


class Follower(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    follower_user = models.CharField(max_length=100, null=True)

    # def __str__(self):
    #     return self.follower_user.username
class Chat(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    typing_user = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    comment_text = models.CharField(default="Enter Comment Here", max_length=2000)
class Message(models.Model):
    chat=models.ForeignKey(Chat,on_delete=models.CASCADE, null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    message=models.CharField(max_length=1000)