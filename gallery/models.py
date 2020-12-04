from django.db import models


class Gallery(models.Model):
    owner = models.ForeignKey('user.User', on_delete=models.CASCADE, blank=False, null=True)
    title = models.CharField(blank=False, null=True,max_length=20)
    subtitle = models.CharField(blank=True, null=True,max_length=20)
    image = models.ImageField('Фото', upload_to='gallery/', blank=True, null=True)
    is_vip = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


class Image(models.Model):
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE, blank=False, null=True,related_name='images')
    image = models.ImageField('Фото', upload_to='gallery/', blank=True, null=True)



