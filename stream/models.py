from django.db import models
from user.services import create_random_string


class Stream(models.Model):
    streamer = models.ForeignKey('user.User',on_delete=models.CASCADE,blank=True,null=True,related_name='streams')
    uid = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='streams/', blank=True, null=True)
    is_vip = models.BooleanField(default=False)
    is_private = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_archived = models.BooleanField(default=False)
    start = models.DateTimeField(blank=True, null=True)
    stop = models.DateTimeField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)


    def save(self, *args, **kwargs):
        if not self.uid:
            self.uid = create_random_string(digits=False,num=8)
        super(Stream, self).save(*args, **kwargs)

    def get_stream_url(self):
        return f'{self.streamer.nickname}--{self.uid}'
