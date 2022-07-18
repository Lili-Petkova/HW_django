from django.db import models


class City(models.Model):
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.city


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class Client(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    product = models.ManyToManyField(Product)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Supplier(models.Model):
    name = models.CharField(max_length=100)
    city = models.OneToOneField(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
