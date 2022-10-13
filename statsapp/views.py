from django.shortcuts import render
from django.views import View
from userapp.models import *
from asosiy. models import *
from .models import *

class StatsView(View):
    def get(self,request):
        ombor = Omborxona.objects.get(user=request.user)
        stats = Stats.objects.filter(Ombor=ombor)
        soz = request.GET.get('soz')
        if soz is None:
            stats = Stats.objects.filter(Ombor=ombor)
        elif soz:
            new = stats.filter(Mahsulot__brend=soz) | stats.filter(Mahsulot__nom=soz)
            new = new | stats.filter(Client__nom=soz) | stats.filter(Client__ism=soz)
            if soz.isdigit():
                new = new | stats.filter(nasiya=soz) | stats.filter(sana__contains=soz)
            stats = new
        data = {
            "stats":stats
        }
        return render(request,'stats.html',data)


