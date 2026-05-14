from django.urls import path
from .views import RegisterView

app_name ="userauth"

urlpatterns = [
    path('sign-up/',RegisterView,name="sign-up"),

]