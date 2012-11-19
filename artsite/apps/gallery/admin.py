from django.contrib import admin
from models import Category, Series, Work


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class SeriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class WorkAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Series, SeriesAdmin)
admin.site.register(Work, WorkAdmin)