from django.db import models


# Create your models here.

class NewProduct(models.Model):
    nam = models.CharField(max_length=2500)
    pric = models.FloatField(default=0.0)
    descriptio = models.TextField
    coun = models.IntegerField(default=0)
    is_activ = models.BooleanField(default=False)
    def to_json(self):
        return {
            'nam': self.nam,
            'pric': self.pric,
            'descriptio': self.descriptio,
            'coun': self.coun,
            'is_activ': self.is_activ
        }

class NewCategories(models.Model):
    nam = models.CharField(max_length=2500)
    def to_Json(self):
        return {
            'nam': self.nam
        }
