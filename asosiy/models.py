from django.db import models
from userapp.models import *

class Mahsulot(models.Model):
    nom = models.CharField(max_length=50)
    narx = models.PositiveIntegerField()
    brend = models.CharField(max_length=50)
    miqdor = models.CharField(max_length=50)
    olvchov = models.CharField(max_length=50,choices=(('KG','KG'),('TONN','TONN')))
    kelgan_sana = models.DateField(auto_now_add=True)
    Ombor = models.ForeignKey(Omborxona,on_delete=models.CASCADE)
    def __str__(self):
        return self.nom

class Client(models.Model):
    ism = models.CharField(max_length=50)
    nom = models.CharField(max_length=50)
    tel = models.CharField(max_length=15)
    qarz = models.CharField(max_length=50)
    manzil = models.CharField(max_length=50)
    Ombor = models.ForeignKey(Omborxona,on_delete=models.CASCADE)
    def __str__(self):
        return self.nom

