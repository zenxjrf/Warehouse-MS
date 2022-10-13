from django.urls import path, include
from userapp.views import *
from asosiy.views import *
from django.contrib import admin
from statsapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',loginview.as_view()),
    path('bulimlar/', include('asosiy.urls')),
    path('logout/',logoutview.as_view()),
    path('stats/',StatsView.as_view()),

]
