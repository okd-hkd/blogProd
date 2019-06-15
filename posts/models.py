from django.db import models
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    published = models.DateTimeField()
    image = models.ImageField(upload_to='media/', blank=True, null=True)  # ドメイン + MEDIA_URL + upload_to に画像を保存してpathをDBに保存
    body = MarkdownxField('body', help_text='Markdown')

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:40]

    def body_to_markdown(self):
        return markdownify(self.body)


    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.id})
