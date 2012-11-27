from django.contrib import admin
from models import Category, Series, Work


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class SeriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class WorkAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    fieldsets = (
        ('Main', {
            'classes': ('collapse',),
            'fields': ('series', 'name', 'slug', 'description', 'image', 'order', 'is_primary_image', 'tags')
        }),
        ('Dimensions', {
            'classes': ('collapse',),
            'fields': ('height', 'width', 'depth')
        }),
        ('Quote', {
            'classes': ('collapse',),
            'fields': ('quote', 'quote_byline')
        }),
        ('SEO', {
            'classes': ('collapse',),
            'fields': ('meta_title', 'meta_description', 'meta_keywords')
        }),
    )

admin.site.register(Category, CategoryAdmin)
admin.site.register(Series, SeriesAdmin)
admin.site.register(Work, WorkAdmin)