from django.shortcuts import render, redirect
from django.views import View
from .models import *
from userapp.models import Omborxona


class Bulimlar(View):
    def get(self,request):
        return render(request,'bulimlar.html')


class Mahsulotlar(View):
    def post(self,request):
        ombor = Omborxona.objects.get(user=request.user)
        Mahsulot.objects.create(
            nom = request.POST.get('pr_name'),
            narx = request.POST.get('pr_price'),
            brend = request.POST.get('pr_brand'),
            miqdor = request.POST.get('pr_amount'),
            Ombor = ombor

        )
        return redirect('/bulimlar/mahsulotlar/')
    def get(self,request):
        ombor = Omborxona.objects.get(user=request.user)
        data ={
            "mahsulotlar":Mahsulot.objects.filter(Ombor=ombor)
        }
        return render(request,'products.html',data)


class mahdel(View):
    def get(self,request,pk):
        m = Mahsulot.objects.get(id=pk)
        ombor = Omborxona.objects.get(user=request.user)
        if ombor == m.Ombor:
            m.delete()
        return redirect("/bulimlar/mahsulotlar/")

class Mahup(View):
    def post(self,request,pk):
        m = Mahsulot.objects.get(id=pk)
        if m.Ombor == Omborxona.objects.get(user=request.user):
            m.nom = request.POST.get('name')
            m.narx = request.POST.get('price')
            m.brand = request.POST.get('brand_name')
            m.miqdor = request.POST.get('amount')
            m.save()

        return redirect('/bulimlar/mahsulotlar/')
    def get(self,request,pk):
        data = {
            "product":Mahsulot.objects.get(id=pk)
        }
        return render(request,'product_update.html',data)

class Clients(View):
    def get(self,request):
        ombor = Omborxona.objects.get(user=request.user)
        data = {
        "clients": Client.objects.filter(Ombor=ombor)
        }
        return render(request, 'clients.html', data)
    def post(self,request):
        ombor = Omborxona.objects.get(user=request.user)
        Client.objects.create(
            ism=request.POST.get('client_name'),
            nom=request.POST.get('client_shop'),
            tel=request.POST.get('client_phone'),
            manzil=request.POST.get('client_address'),
            Ombor = ombor
        )
        return redirect('/bulimlar/clients/')


class Clientdel(View):
    def get(self, request, pk):
        m = Client.objects.get(id=pk)
        ombor = Omborxona.objects.get(user=request.user)
        if ombor == m.Ombor:
            m.delete()
        return redirect("/bulimlar/clients/")

    def post(self,request,pk):
        m = Client.objects.get(id=pk)
        if m.Ombor == Omborxona.objects.get(user=request.user):
            m.ism = request.POST.get('client_name')
            m.nom = request.POST.get('client_shop')
            m.tel = request.POST.get('client_phone')
            m.manzil = request.POST.get('client_address')
            m.save()

        return redirect('/bulimlar/mahsulotlar/')

