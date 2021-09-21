from django.db import models


# Create your models here.
class PCModel(models.Model):
    class Meta:
        db_table = 'comps'

    brand = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    ram = models.IntegerField()
    freq = models.IntegerField()
    monitor = models.CharField(max_length=255)
