
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import logout,login,authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from django import forms




def check_choices(request):
    return render(request,"choices_box.html",{})




def select(request):
    return render(request,"choices_box.html",{})





def not_select(request):
    return render(request,"choices_box.html",{})




def select_again(request):
    return render(request,"choices_box.html",{})