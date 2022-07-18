from django.db import models


class New_register(models.Model):
    email=models.CharField(max_length=200)
    name=models.CharField(max_length=200)
    password=models.CharField(max_length=200)

class students(models.Model):
    Name=models.CharField(max_length=200)
    Branch=models.CharField(max_length=200)
    Document=models.CharField(max_length=200)

class result(models.Model):
    Name=models.CharField(max_length=200)
    Branch=models.CharField(max_length=200)
    Document=models.CharField(max_length=200)
class assignment(models.Model):
    Name=models.CharField(max_length=200)
    Branch=models.CharField(max_length=200)
    Document=models.CharField(max_length=200)






# Create your models here.
