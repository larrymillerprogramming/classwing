from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Material(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="materials")
    isCourse = models.BooleanField(default=False)
    title = models.CharField(max_length=100, null=False)
    author = models.CharField(max_length=100, null=False)
    startDate = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return f"{self.title}"

    def serialize(self):
        return {
            "id": self.id,
            "owner": self.owner.username,
            "title": self.title,
            "author": self.author,
            "startDate": self.startDate
        }

class Post(models.Model):
    poster = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    about = models.ForeignKey(Material, on_delete=models.CASCADE, related_name="postsabout", null=True)
    content = models.CharField(max_length=500, null=True)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.poster}: {self.time}"

    def serialize(self):
        return {
            "id": self.id,
            "poster": self.poster.username,
            "time": self.time
        }

class Follow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name="following", null=True)
    account = models.ForeignKey(User, on_delete=models.CASCADE, related_name="followers", null=True)
    is_following = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.follower} follows {self.account}"

    def serialize(self):
        return {
            "id": self.id,
            "follower": self.follower.username,
            "account": self.account.username,
            "is_following": self.is_following
        }

class Like(models.Model):
    liker = models.ForeignKey(User, on_delete=models.CASCADE, related_name="likedPosts", null=True)
    postId = models.CharField(max_length=1000, null=True)
    is_liked = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.liker} likes Post: {self.postId}"

    def serialize(self):
        return {
            "id": self.id,
            "liker": self.liker.username,
            "postId": self.postId,
            "is_liked": self.is_liked
        }