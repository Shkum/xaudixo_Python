from django.db import models
import datetime
from django.utils import timezone


class Article(models.Model):
    article_title = models.CharField('article name', max_length=200)
    article_text = models.TextField('article text')
    pub_date = models.DateTimeField('publication date')

    def __str__(self):
        return self.article_title

    def was_published_recently(self):
        return self.pub_date >= (timezone.now() - datetime.timedelta(days=7))

    #  for changing name in list of items in admin page (single and plural)
    class Meta:
        verbose_name = 'Single article (change in model.py)'
        verbose_name_plural = 'Many articles (change in model.py)'


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author_name = models.CharField('author`s name', max_length=50)
    comment_text = models.CharField('comment text', max_length=200)

    def __str__(self):
        return self.author_name

    class Meta:
        verbose_name = 'Single comment (change in model.py)'
        verbose_name_plural = 'Many comments (change in model.py)'
