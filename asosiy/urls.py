from django.urls import path
from .views import *
urlpatterns = [
    path('clients/',Clients.as_view()),
    path('stats/',Bulimlar.as_view()),
    path('mahsulotlar/',Mahsulotlar.as_view()),
    path('',Bulimlar.as_view()),
    path('mahdelete/<int:pk>/',mahdel.as_view()),
    path('Mahupdate/<int:pk>',Mahup.as_view()),
]