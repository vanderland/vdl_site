
from django.db import models
# from autoslug import AutoSlugField
from django.urls import reverse


class Page(models.Model):
    title = models.CharField('Title', max_length=150)
    body = models.TextField('Body')
    slug = models.SlugField()
    # slug        = AutoSlugField(populate_from='title')
    created_on = models.DateTimeField('Created On', auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['created_on']
        verbose_name = 'Page'
        verbose_name_plural = 'Pages'

    def get_absolute_url(self):
        return reverse('detail', kwargs={'slug': self.slug})
