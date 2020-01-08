from django.db import models
from django.urls import reverse
from .Kmean import Kmean
import os
# Create your models here.

# Create class Collage with attributes 
class Collage(models.Model):
    # upload image background
    background_image = models.ImageField()
    # upload image has the objects
    objects_iamge = models.ImageField()

    # function for click submit
    def get_absolute_url(self):
        temp = Kmean(self.background_image.name, self.objects_iamge.name)
        goal_image = temp.processing()
        return reverse('collage:index')
