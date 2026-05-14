from django.shortcuts import render,redirect
from userauth.models import User,Profile
from userauth.forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout


def RegisterView(request):
    if request.user.is_authenticated:
        messages.warning(request,f"you are already logged in")
    form=UserRegisterForm(request.POST or None)
    # print("form ===", form)#info

    if form.is_valid():
        form.save()
        full_name = form.cleaned_data.get("full_name")
        phone = form.cleaned_data.get("phone")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password1")

        user =authenticate(email=email,password=password)
        login(request,user)

        messages.success(request,f"hey{full_name},your account has been created successfully")
        
        profile=Profile.objects.get(user=request.user)
        profile.full_name=full_name
        profile.phone=phone
        profile.save()

        return redirect("hotel:index")

    context = {
        "form":form
    }
    return render(request,"userauth/sign-up.html",context)

def logOut(request):
    logout(request)
    messages.success(request,'You have been logged out')
    return redirect('hotel:index')