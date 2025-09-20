from django.contrib import admin
from .models import ServiceStart, Category_Service, ServiceItem
# Register your models here.
@admin.register(ServiceStart)
class ServiceStartAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'title_ar', 'description_ar')
    search_fields = ('title', 'description', 'title_ar', 'description_ar')
    ordering = ('title',)
@admin.register(Category_Service)
class CategoryServiceAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)
@admin.register(ServiceItem)
class ServiceItemAdmin(admin.ModelAdmin):
    list_display = ('service_name', 'service_start', 'slug')
    search_fields = ('service_name', 'service_details', 'service_name_ar', 'service_details_ar')
    ordering = ('service_name',)
    prepopulated_fields = {'slug': ('service_name',)}
    list_filter = ('service_start',)