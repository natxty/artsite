from .models import Response, Log
from django.contrib import admin


class LogAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'author', 'content' )


admin.site.register(Response)
admin.site.register(Log, LogAdmin)
