from django.db import models

# Create your models here.

class types(models.Model):
    name = models.CharField(max_length=150)


    def __str__(self):
        return self.name


class wears(models.Model):
    type = models.ForeignKey(to="types", on_delete=models.CASCADE)
    make = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='Clothes/', blank=True, null=True)


    def __str__(self):
        return f'{self.color} {self.make}'