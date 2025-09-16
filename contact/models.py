from django.db import models

# Create your models here.


class info(models.Model):
    phone_contact = models.IntegerField(max_length=20, null=True, blank=True)
    email_contact = models.EmailField(max_length=25, null=True, blank=True)
    location_contact = models.CharField(max_length=60, null=True, blank=True)
    iframe_map_contact = models.CharField(null=True, blank=True)
    
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Info'
        verbose_name_plural = 'Info'

    def __str__(self):
        return self.email_contact
    


class social_media_info(models.Model):
    icon_name = models.CharField(max_length=255, blank=True, null=True)
    link = models.URLField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = ("social media icon")
        verbose_name_plural = ("social media icons")

    def __str__(self):
        return self.icon_name
    
    