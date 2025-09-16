from django.contrib import admin
from .models import info, social_media_info
# Register your models here.

@admin.register(info)
class InfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'phone_contact', 'email_contact', 'location_contact', 'iframe_map_contact')
    search_fields = ('email_contact', 'location_contact')
    list_filter = ('location_contact',)
    ordering = ('id',)


@admin.register(social_media_info)
class SocialMediaInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'icon_name', 'link', 'created_at', 'updated_at')
    search_fields = ('icon_name', 'link')
    list_filter = ('created_at', 'updated_at')
    ordering = ('id',)
    list_per_page = 20
