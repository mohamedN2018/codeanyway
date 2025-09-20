from django.db import models
from django.utils.text import slugify
# Create your models here.

class ServiceStart(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    title_ar = models.CharField(max_length=200)
    description_ar = models.TextField()

    class Meta:
        verbose_name = "Service Start"
        verbose_name_plural = "Service Starts"

    def __str__(self):
        return self.title
    

class Category_Service(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Category Service"
        verbose_name_plural = "Category Services"

    def __str__(self):
        return self.name

class ServiceItem(models.Model):
    service_start = models.ForeignKey(Category_Service, related_name='service_items', on_delete=models.CASCADE)
    service_name = models.CharField(max_length=255, null=True, blank=True)
    service_name_ar = models.CharField(max_length=255, null=True, blank=True)
    service_details = models.TextField(null=True, blank=True)
    service_details_ar = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='service_items/')
    slug = models.SlugField(unique=True, blank=True, null=True)


    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name or '')
            unique_slug = base_slug
            num = 1

            while ServiceItem.objects.filter(slug=unique_slug).exclude(pk=self.pk).exists():
                unique_slug = f"{base_slug}-{num}"
                num += 1

            self.slug = unique_slug

        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Service Item"
        verbose_name_plural = "Service Items"

    def __str__(self):
        return self.service_name