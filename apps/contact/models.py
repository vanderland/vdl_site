
from django.db import models

class Contact(models.Model):
    name_first      = models.CharField('First Name', max_length=50)
    name_middle     = models.CharField('Middle Name', max_length=50, blank=True, null=False)
    name_last       = models.CharField('Last Name', max_length=50)
    email_address   = models.EmailField('Email Address', max_length=125 )
    subject         = models.CharField('Subject', max_length=150)
    message         = models.TextField('Message')
    created_on      = models.DateTimeField('Created On', auto_now_add=True)

    def __str__(self):
        return self.name_first + ' ' + self.name_last

    class Meta:
        ordering = ['created_on']
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'