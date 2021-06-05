from django.contrib import admin
from .models import Team
from django.utils.html import format_html
# Register your models here.

class TeamAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px;"/>'.format(object.image.url))
    thumbnail.short_description = 'Avatar'
    list_display = ('id', 'thumbnail', 'first_name', 'last_name', 'designation', 'created_at')
    list_display_links = ('id', 'thumbnail', 'first_name')
    search_fields=('id', 'first_name', 'designation')
    list_filter =('designation',)
    ordering= ['id']

admin.site.register(Team, TeamAdmin)
