# from django.db import models
from djongo import models
# Create your models here.

class match(models.Model):
    matched = models.CharField(max_length=2000)
    class Meta:
        abstract = True

class Files(models.Model):
    filename = models.CharField(max_length=200, default="")
    file = models.FileField(upload_to='files')
    matchingcode = models.ArrayField(model_container=match)

    objects = models.DjongoManager()
    def __str__(self):
        return self.filename