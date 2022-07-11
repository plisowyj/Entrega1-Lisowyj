from django.urls import path
from . import views

urlpatterns = [
    path('', views.findex, name='findex'),
    path('add/member/', views.faddmember, name='faddmember'),
    path('add/phone/', views.faddPhones, name='faddPhones'),
    path('add/address/', views.faddAddress, name='faddAddress'),
    path('finder', views.fFinder, name='fFinder'),
]
