from django.db import models
from django.utils.translation import gettext_lazy as _
class Article(models.Model):
    title=models.CharField(verbose_name=_('title'),max_length=255)
    slug=models.SlugField(verbose_name=_('slug'),unique=True)
    text=models.TextField(verbose_name=_('text'))
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title