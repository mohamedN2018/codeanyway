from django.contrib import admin
from .models import factsStart
# Register your models here.

@admin.register(factsStart)
class factsStartAdmin(admin.ModelAdmin):
    list_display = ('icon', 'number', 'title', 'title_ar')
    search_fields = ('title',)
    list_filter = ('number',)
    ordering = ('number',)
    fieldsets = (
        (None, {
            'fields': ('icon', 'number', 'title', 'title_ar')
        }),
    )
