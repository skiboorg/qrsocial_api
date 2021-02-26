from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from pytils.translit import slugify
from random import choices
import string

class BlogItem(models.Model):
    order_num = models.IntegerField('Порядок вывода', default=100)
    name = models.CharField('Название', max_length=255, blank=True, null=True)
    name_slug = models.CharField('Название', max_length=255, blank=True, null=True, editable=False)
    image = models.ImageField('Картинка', upload_to='blog/', blank=True, null=True)
    description = RichTextUploadingField('Статья', blank=True, null=True)
    short_description = models.TextField('Описание', blank=True,null=True)
    is_at_home = models.BooleanField('На главной?', default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ('-order_num',)
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"

    def save(self, *args, **kwargs):

        slug = slugify(self.name)
        if not self.name_slug:
            testSlug = BlogItem.objects.filter(name_slug=slug)
            slugRandom = ''
            if testSlug:
                slugRandom = '-' + ''.join(choices(string.ascii_lowercase + string.digits, k=2))
            self.name_slug = slug + slugRandom
        if self.name:
            self.name_lower = self.name.lower()
        super(BlogItem, self).save(*args, **kwargs)
