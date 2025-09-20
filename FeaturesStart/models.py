from django.db import models

# Create your models here.

class FeatureStart(models.Model):
    Title_Feature = models.CharField(max_length=200)
    description_Feature = models.TextField()
    Title_Feature_ar = models.CharField(max_length=200)
    description_Feature_ar = models.TextField()
    images_Feature = models.ImageField(upload_to='features/')
    created_at_Feature = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at_Feature']  
        verbose_name = "Feature Start"
        verbose_name_plural = "Feature Starts"


    def __str__(self):
        return self.Title_Feature
    


class FeatureItem(models.Model):
    title_item = models.CharField(max_length=200)
    description_item = models.TextField()
    title_item_ar = models.CharField(max_length=200)
    description_item_ar = models.TextField()
    icon_item = models.CharField(max_length=100)  # Assuming you store icon names or paths as strings
    created_at_item = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at_item']  
        verbose_name = "Feature Item"
        verbose_name_plural = "Feature Items"

    def __str__(self):
        return self.title_item
    