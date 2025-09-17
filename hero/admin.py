from django.contrib import admin
from .models import HeroSlider, Hero
# Register your models here.


@admin.register(HeroSlider)
class HeroSliderAdmin(admin.ModelAdmin):
    list_display = ('title_site', 'created_at')
    search_fields = ('title_site',)
    list_filter = ('created_at',)
    ordering = ('-created_at',)
    readonly_fields = ('created_at',)
    fieldsets = (
        (None, {
            'fields': ('title_site', 'title_site_ar', 'logo_site', 'logo_site_ar', 'favicon_site')
        }),
        ('Metadata', {
            'fields': ('created_at',),
            'classes': ('collapse',),
        }),
    )

@admin.register(Hero)
class HeroAdmin(admin.ModelAdmin):
    list_display = ('title_hero', 'created_at_hero')
    search_fields = ('title_hero',)
    list_filter = ('created_at_hero',)
    ordering = ('-created_at_hero',)
    readonly_fields = ('created_at_hero',)
    fieldsets = (
        (None, {
            'fields': ('title_hero', 'title_hero_ar', 'subtitle_hero', 'subtitle_hero_ar', 'image_hero_car')
        }),
        ('Metadata', {
            'fields': ('created_at_hero',),
            'classes': ('collapse',),
        }),
    )