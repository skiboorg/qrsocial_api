from django.db import models


def humanize_time(time):
    from django.utils.timesince import timesince
    return timesince(time)

class Post(models.Model):
    owner = models.ForeignKey('user.User', on_delete=models.CASCADE, blank=False, null=True)
    text = models.TextField(blank=False, null=True)
    image = models.ImageField('Фото', upload_to='posts/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_comments_count(self):
        return self.comments.count()

    def get_humanize_time(self):
        return humanize_time(self.created_at)

    def user_likes(self, obj):
        return obj.likes.all()


class PostComment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, blank=False, null=True,related_name='comments')
    owner = models.ForeignKey('user.User', on_delete=models.CASCADE, blank=False, null=True)
    text = models.TextField(blank=False, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_humanize_time(self):
        return humanize_time(self.created_at)

class PostLike(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, blank=False, null=True,related_name='likes')
    users = models.ManyToManyField('user.User', blank=True)



