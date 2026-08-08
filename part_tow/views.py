from part_one.models import Character
from .box_choices import Box
from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from django.contrib.auth import logout,login,authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from django import forms
from django.http import JsonResponse



def check_choices(request):
    return render(request,"choices_box.html",{})




def select(request):
    person_box=Box(request)
    if request.POST.get('action')== 'post':
        character_id=int(request.POST.get('character_id'))
        character=get_object_or_404(Character,id= character_id)
        person_box.add(character=character)

        response=JsonResponse({"character_name":character.First_name})
        return response



def not_select(request):
    return render(request,"choices_box.html",{})




def select_again(request):
    return render(request,"choices_box.html",{})