from django.db import models

# Create your models here.

class About(models.Model):
    smalltext = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    description_title = models.CharField(max_length=200)
    
    image = models.ImageField(upload_to='about_images/')

    class Meta:
        verbose_name = "About"
        verbose_name_plural = "Abouts"


    def __str__(self):
        return self.title        
    


class DetailsSmall(models.Model):
    icon = models.CharField(max_length=100)
    title = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Detail"
        verbose_name_plural = "Details"

    def __str__(self):
        return self.title
    

 # Arabic Models
class About_Ar(models.Model):
    smalltext = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    description_title = models.CharField(max_length=200)
    
    image = models.ImageField(upload_to='about_images/')

    class Meta:
        verbose_name = "About AR"
        verbose_name_plural = "Abouts AR"


    def __str__(self):
        return self.title        
    

 # Arabic Models
class DetailsSmall_Ar(models.Model):
    icon = models.CharField(max_length=100)
    title = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Detail AR"
        verbose_name_plural = "Details AR"

    def __str__(self):
        return self.title
    