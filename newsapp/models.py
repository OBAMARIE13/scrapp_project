from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class Source(models.Model):
	name = models.CharField(max_length=255)
	link = models.URLField()
	date_add = models.DateTimeField(auto_now_add=True)
	date_update = models.DateTimeField(auto_now=True)
	status = models.BooleanField(default=True)

	class Meta:
		verbose_name = 'Source'
		verbose_name_plural = 'Sources'

	def __str__(self):
		return self.name

class Category(models.Model):
	name = models.CharField(max_length=255)
	date_add = models.DateTimeField(auto_now_add=True)
	date_update = models.DateTimeField(auto_now=True)
	status = models.BooleanField(default=True)

	class Meta:
		verbose_name = 'Category'
		verbose_name_plural = 'Categorys'

	def __str__(self):
		return self.name

class Tag(models.Model):
	name = models.CharField(max_length=255)
	date_add = models.DateTimeField(auto_now_add=True)
	date_update = models.DateTimeField(auto_now=True)
	status = models.BooleanField(default=True)

	class Meta:
		verbose_name = 'Tag'
		verbose_name_plural = 'Tags'

	def __str__(self):
		return self.name

class Article(models.Model):
	title = models.TextField()
	picture = models.TextField()
	link_detail = models.TextField()
	description = HTMLField()
	date_publication = models.TextField()
	source = models.ForeignKey('newsapp.Source', related_name='source_article', on_delete=models.CASCADE)
	category = models.ForeignKey('newsapp.Category', related_name='category_article', on_delete=models.CASCADE, blank=True)
	tag = models.ManyToManyField('newsapp.Tag', related_name='tag_article', blank=True)
	date_add = models.DateTimeField(auto_now_add=True)
	date_update = models.DateTimeField(auto_now=True)
	status = models.BooleanField(default=True)

	class Meta:
		verbose_name = 'Article'
		verbose_name_plural = 'Articles'

	def __str__(self):
		return self.title

	def save(self, *args, **kw):
		return super().save(*args, **kw)
