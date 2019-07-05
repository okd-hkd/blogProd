from django.db import models
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify
from django.utils.translation import gettext_lazy as _


#Create your models here.

class CategoryOfPost(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Post(models.Model):

     title = models.CharField(max_length=100)
     category = models.ForeignKey(CategoryOfPost, on_delete=models.SET_NULL, blank=True, null=True)
     published = models.DateTimeField()
     released_date = models.DateTimeField(
            blank=True, null=True)
     image = models.ImageField(upload_to='media/', blank=True, null=True)  # ドメイン + MEDIA_URL + upload_to に画像を保存してpathをDBに保存
     body = MarkdownxField('body', help_text='Markdown')

# on_delete=models.SET_NULL, null=True

     def __str__(self):
         return self.title

     def summary(self):
         return self.body[:40]

     def body_to_markdown(self):
         return markdownify(self.body)

     def get_absolute_url(self):
         return reverse('post_detail', kwargs={'pk': self.id})

