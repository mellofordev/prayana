from django.db import models

# Create your models here.
years = (('1,','First'),('2','Second'),('3','Third'),('4','Fourth'))
class Student(models.Model):
    name = models.CharField(max_length=20)
    year = models.CharField(max_length=10,choices=years,default='1')
    blood_group = models.CharField(max_length=10)
    phone = models.IntegerField()

    def __str__(self) -> str:
        return self.name