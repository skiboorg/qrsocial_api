from django.db import models


class Gallery(models.Model):
    owner = models.ForeignKey('user.User', on_delete=models.CASCADE, blank=False, null=True)
    title = models.CharField(blank=False, null=True,max_length=20)
    subtitle = models.CharField(blank=True, null=True,max_length=20)
    image = models.ImageField('Фото', upload_to='gallery/', blank=True, null=True)
    is_vip = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering = ('-created_at',)


class Image(models.Model):
    owner = models.ForeignKey('user.User', on_delete=models.CASCADE, blank=False, null=True)
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE, blank=False, null=True,related_name='images')
    image = models.ImageField('Фото', upload_to='gallery/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

class Banner(models.Model):
    image = models.ImageField('Баннер', upload_to='banner/', blank=True, null=True)



class Video(models.Model):
    owner = models.ForeignKey('user.User', on_delete=models.CASCADE, blank=False, null=True)
    title = models.CharField(blank=False, null=True,max_length=20)
    image = models.ImageField('Фото', upload_to='gallery/video/image/', blank=True, null=True)
    file = models.FileField('Файл', upload_to='gallery/video/', blank=True, null=True)
    is_vip = models.BooleanField(default=False)
    show_at_index = models.BooleanField(default=False)
    views = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
