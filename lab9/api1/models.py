from django.db import models


# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(default='')
    city = models.CharField(max_length=300)
    address = models.TextField(default='')

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'
        # ordering = ('name',)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'city': self.city,
            'address': self.address
        }

    def __str__(self):
        return f'{self.id}: {self.name}'


class Vacancy(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(default='')
    salary = models.FloatField(default=0.0)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True,
                                related_name='vacancies')

    # tags = models.ManyToManyField(Tag)

    class Meta:
        verbose_name = 'Vacancy'
        verbose_name_plural = 'Vacancies'

    def __str__(self):
        return f'{self.id}: {self.name} | {self.salary}'

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'salary': self.salary
        }





















class NewProduct(models.Model):
    nam = models.CharField(max_length=2500)
    pric = models.FloatField(default=0.0)
    # descriptio = models.TextField
    coun = models.IntegerField(default=0)
    is_activ = models.BooleanField(default=False)

    def to_json(self):
        return {
            'nam': self.nam,
            'pric': self.pric,
            # 'descriptio': self.descriptio,
            'coun': self.coun,
            'is_activ': self.is_activ
        }


class NewCategories(models.Model):
    nam = models.CharField(max_length=2500)

    def to_Json(self):
        return {
            'nam': self.nam
        }
