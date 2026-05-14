from django.urls import path
from .views import index

app_name = "hotel"

urlpatterns = [
    path('',index,name="index"),

]