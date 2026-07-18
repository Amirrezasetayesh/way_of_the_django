from django.shortcuts import render,HttpResponse,redirect
from .models import Character,Personal_data
from django.contrib.auth import logout,login,authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from django import forms
from .forms import SignupForm
def first_per(rq):
    return HttpResponse("<h1>the first person is amir</h1>")

# HttpResponse just return some html code to persons like below code
def main_page(rq):

    # with below code you can give access to you database models
    # all_person=Person.objects.all()
    characters_datas=Personal_data.objects.all()
    # i make the person data for my render method
    return render(rq,"home.html",{'characters_data':characters_datas})


# home == main_mage


#     in html file you when you want to use your model you should use the key ==>>'anything' and not value
# render is for your models, and it can show some html pages to persons
# render receives one rq (the rq of your def) and one location for you html file from the templates

def second_per(rq):
    return HttpResponse("<h1> the second person is reza</h1>")



def gran_line(rq):
    return render(rq,"grand_line_page.html")

def login_user(request):
    if request.method=="POST":
        # we give the information from POST method pay attention we set the POST method in our html file
        username_user=request.POST['username']
        # we give the username and password form the POST method datas
        password_user=request.POST['password']


        user=authenticate(request,username=username_user,password=password_user)
        # authenticate method is for check the username and password of person for login
        if user is not None:
            # if user does exist you should login the user in our site
            login(request,user)
            # login method is done the
            messages.success(request,"login was successful")
            # if the return of code was true you tell me the message
            return redirect("main_page")
        # and now take me to main page please with redirect
        else:
            messages.success(request,"login was not successful")
            # else tell me this messages
            return redirect("login_user_site")
    else:
        # if you did not give any POST method from front end you should render and check the login template
        return render(request,'login.html')




def logout_user(request):
    logout(request)
    messages.success(request,"logout was success full")
    return redirect("main_page")



def signup_user(request):
    form=SignupForm()
    # at the first you should make you own form in this view, pay attention you before you call this form you should already make this form in forms.py
    # you should make the forms.py in you app
    if request.method=="POST":
        # again you should give the introductions from POST method and check it
        form=SignupForm(request.POST)
        # you should pour the data from POST method to your own form
        if form.is_valid:
            # if all the parameters is true and the person add the information to form , you should chek the form values=== is_valid
            form.save()
            # and now you should save information for one user in site
            username=form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            # this Process is like login or equal login Process
            login(request,user)
            messages.success(request,"signup was successful")
            return redirect("main_page")
        else:
            messages.success(request,"login was not successful")
            return redirect("signup_user_site")
    else:
        # if you do not give any data from POST method you can check again signup_user_site template
        return render(request,'signup.html',{'form':form})