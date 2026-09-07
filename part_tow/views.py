from part_one.models import Character
from .box_choices import Box
from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from django.contrib.auth import logout,login,authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from django import forms
from django.http import JsonResponse



def check_choices(request):
    box=Box(request)
    box_character=box.get_character()
    quantities=box.get_quants()
    return render(request,"choices_box.html",{"box_character":box_character,"quantity":quantities})




def select(request):
    person_box=Box(request)
    if request.POST.get('action')== 'post':

        character_id = int(request.POST.get('character_id'))

        character=get_object_or_404(Character,id= character_id)

        character_qty = int(request.POST.get('character_qty'))

        person_box.add(character=character,quantity=character_qty)

        # response=JsonResponse({"character_name":character.First_name})
        gift_qty=person_box.__len__()
        # up line just for calculate of the sum character chose
        response = JsonResponse({"qty": gift_qty})
        #
        return response



def not_select(request):
    return render(request,"choices_box.html",{})




def select_again(request):
    return render(request,"choices_box.html",{})