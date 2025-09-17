from django.db import models

# Create your models here.

class HeroSlider(models.Model):
    title_site = models.CharField(max_length=200)
    title_site_ar = models.CharField(max_length=200)
    logo_site = models.ImageField(upload_to='hero_images/')
    logo_site_ar = models.ImageField(upload_to='hero_images/')
    favicon_site = models.ImageField(upload_to='hero_images/')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Hero Slider"
        verbose_name_plural = "Hero Sliders"

    def __str__(self):
        return self.title_site


class Hero(models.Model):
    title_hero = models.CharField(max_length=200)
    title_hero_ar = models.CharField(max_length=200)
    subtitle_hero = models.CharField(max_length=300)
    subtitle_hero_ar = models.CharField(max_length=300)
    image_hero_car = models.ImageField(upload_to='hero_images/')
    created_at_hero = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Hero Section"
        verbose_name_plural = "Hero Sections"

    def __str__(self):
        return self.title_hero
    


