from django.shortcuts import render,HttpResponse
from .models import Character,Personal_data
from django.contrib.auth import logout,login,authenticate
from django.contrib import redirects


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

def log_in(rq):
    pass




def log_out(rq):
    pass




