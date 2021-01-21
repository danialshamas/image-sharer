from django.db import models
from sorl.thumbnail import ImageField
# Create your models here.
class Feed_post(models.Model):
    text = models.CharField(max_length=140, blank=False, null=False)
    image = models.ImageField()

    def __str__(self):
        return self.text

