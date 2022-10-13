from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import View


class loginview(View):
    def get(self,request):
        return render(request,'home.html')
    def post(self,request):
        user = authenticate(username=request.POST.get('login'),password=request.POST.get('password'))
        if user is None:
            return redirect('/home/')
        login(request,user)
        return redirect('/bulimlar/')

class logoutview(View):
    def get(self,request):
        logout(request)
        return redirect("/home/")
