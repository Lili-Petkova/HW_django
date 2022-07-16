from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=200)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Log(models.Model):
    path = models.CharField(max_length=300)
    method = models.CharField(max_length=300)
    timestamp = models.DateField(auto_now_add=True)
