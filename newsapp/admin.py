from django.contrib import admin
from . import models
from django.utils.safestring import mark_safe
from django.utils.safestring import mark_safe

# Register your models here.

@admin.register(models.Source)
class SourceAdmin(admin.ModelAdmin):
	list_display = ('name', 'link', 'date_add', 'date_update', 'status')
	date_hierarchy = 'date_add'
	list_per_page = 10
	list_editable = ['link', 'status']

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ('name', 'date_add', 'date_update', 'status')
	date_hierarchy = 'date_add'
	list_per_page = 10
	list_editable = ['status']

@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
	list_display = ('name', 'date_add', 'date_update', 'status')
	date_hierarchy = 'date_add'
	list_per_page = 10
	list_editable = ['status']

@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
	list_display = ('picture_view', 'title', 'source', 'date_publication', 'date_add', 'date_update', 'status')
	date_hierarchy = 'date_add'
	list_per_page = 10
	filter_horizontal = ['tag']
	list_editable = ['status']
	
	def picture_view(self, obj):
		return mark_safe(f'<img src="{obj.picture}" style="height:100px; width:150px">')
	picture_view.short_description = 'Aperçu des images' 

