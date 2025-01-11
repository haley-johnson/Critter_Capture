from django.db import models

# Create your models here.
class Animal_Log(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    loc = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Animals(models.Model):
    name = models.CharField(max_length=100)
    # photo = models.ImageField(upload_to='/photos')

    def __str__(self):
        return self.name