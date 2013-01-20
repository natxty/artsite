from django.contrib import admin
from models import Category, Work


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class WorkAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    fieldsets = (
        ('Main', {
            'fields': ('category', 'name', 'slug', 'description', 'image', 'order', 'is_primary_image', 'tags')
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
admin.site.register(Work, WorkAdmin)