from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('Home/',views.Home,name="HomePage"),
    path('AboutUs/',views.About,name="AboutUs Page"),
    path('Orders/',views.order,name="Order Page"),
]
