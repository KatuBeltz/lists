from django.db import models

class Collection(models.Model):
    name = models.CharField('Name', max_length=32)
    file = models.FileField(upload_to='collection_files')
