from django.db import models

# Create your models here.

class factsStart(models.Model):
    icon = models.CharField(max_length=100)
    number = models.IntegerField(default=0)
    title = models.CharField(max_length=100)
    title_ar = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = 'Facts Start'
        verbose_name_plural = 'Facts Starts'

    def __str__(self):
        return self.title