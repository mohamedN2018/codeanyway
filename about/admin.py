from django.contrib import admin
from .models import About, DetailsSmall, About_Ar, DetailsSmall_Ar
# Register your models here.

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'smalltext', 'description_title', 'image')
    search_fields = ('title', 'smalltext', 'description_title')
    list_per_page = 20
    ordering = ('title',)

@admin.register(DetailsSmall)
class DetailsSmallAdmin(admin.ModelAdmin):
    list_display = ('icon', 'title')
    search_fields = ('title',)
    list_per_page = 20
    ordering = ('title',)


@admin.register(About_Ar)
class AboutArAdmin(admin.ModelAdmin):
    list_display = ('title', 'smalltext', 'description_title', 'image')
    search_fields = ('title', 'smalltext', 'description_title')
    list_per_page = 20
    ordering = ('title',)



@admin.register(DetailsSmall_Ar)
class DetailsSmallArAdmin(admin.ModelAdmin):
    list_display = ('icon', 'title')
    search_fields = ('title',)
    list_per_page = 20
    ordering = ('title',)