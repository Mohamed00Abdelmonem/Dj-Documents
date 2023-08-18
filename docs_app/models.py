from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.translation import gettext_lazy as _ 
# Create your models here.


class Category(models.Model):
    name = models.CharField(_('Name'),max_length=100)
    intro = models.TextField(_('Intro'))
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='category_author', verbose_name=_('Author'))
    created_at = models.DateTimeField(_('Created AT'),default= timezone.now)

    def __str__(self):
        return self.name
    


class Document(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='document_user' , verbose_name=_('Document'))
    title = models.CharField(_('Title'),max_length=100)
    content = models.TextField(_('Content'))
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='document_author', verbose_name=_('Author'))
    created_at = models.DateTimeField(_('Created AT'),default= timezone.now)
    
    def __str__(self):
        return self.title - self.category
 