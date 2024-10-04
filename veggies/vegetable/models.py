from django.db import models

class Vegetable(models.Model):
    veg_id = models.IntegerField()
    veg_name = models.CharField(max_length=100)
    veg_image = models.ImageField(upload_to='vegetable_images/')

    def __str__(self):
        return self.veg_name

