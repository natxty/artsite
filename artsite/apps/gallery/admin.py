from django.contrib import admin
from models import Category, Work, Link


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

    list_display_links = ('__unicode__', )
    list_display = ('__unicode__', 'name', 'slug', 'order', 'order_link' )

    def order_link(request, self):
        return '<a href="/admin/order/%s/">Order %s</a>' % (self.slug, self.name)
    
    order_link.allow_tags = True #this is to allow HTML tags.
    order_link.short_description = 'Order by Thumbnail'  



class WorkAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    #Sortable Admin Stuff:

    list_display_links = ('__unicode__', )
    list_display = ('__unicode__', 'name', 'slug', 'category', 'date_created', 'order' )


    fieldsets = (
        ('Main', {
            'fields': ('category', 'name', 'slug', 'image', 'date_created', 'medium', 'description', 'notes', 'order', 'is_primary_image', 'tags')
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
    
class LinkAdmin(admin.ModelAdmin):
    list_display = ('title', 'active', 'order')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Work, WorkAdmin)
admin.site.register(Link, LinkAdmin)