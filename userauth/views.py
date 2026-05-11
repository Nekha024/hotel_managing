from django.shortcuts import render
from userauth.models import User,Profile
from userauth.forms import UserRegisterForm

def RegisterView(request):
    form=UserRegisterForm(request.POST or None)
    print("form ===", form)#info

    # if form.is_valid():
    #     form.save()
    #     full_name = form.cleaned_data.get("full_name")
    #     print("full name ===", full_name)#info
    context = {
        "form":form
    }
    return render(request,"userauth/sign-up.html",context)