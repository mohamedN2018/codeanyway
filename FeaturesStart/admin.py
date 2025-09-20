from django.contrib import admin
from .models import FeatureStart, FeatureItem
# Register your models here.

@admin.register(FeatureStart)
class FeatureStartAdmin(admin.ModelAdmin):
    list_display = ('Title_Feature', 'created_at_Feature')
    search_fields = ('Title_Feature',)
    ordering = ('-created_at_Feature',) 
    fieldsets = (
        (None, {
            'fields': ('Title_Feature', 'description_Feature', 'Title_Feature_ar', 'description_Feature_ar', 'images_Feature')
        }),

    )

@admin.register(FeatureItem)
class FeatureItemAdmin(admin.ModelAdmin):
    list_display = ('title_item', 'created_at_item')
    search_fields = ('title_item',)
    ordering = ('-created_at_item',) 
    fieldsets = (
        (None, {
            'fields': ('title_item', 'description_item', 'title_item_ar', 'description_item_ar', 'icon_item')
        }),
    )