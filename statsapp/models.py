from django.db import models
from asosiy.models import *

class Stats(models.Model):
    Client = models.ForeignKey(Client,on_delete=models.CASCADE)
    Mahsulot = models.ForeignKey(Mahsulot,on_delete=models.CASCADE)
    umumiy = models.IntegerField()
    miqdor = models.IntegerField()
    sana = models.DateTimeField(auto_now_add=True)
    tolandi = models.IntegerField()
    nasiya = models.PositiveIntegerField()
    Ombor = models.ForeignKey(Omborxona,on_delete=models.CASCADE)