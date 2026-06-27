from django.shortcuts import render,HttpResponse

# Create your views here.



def first_per(rq):
    return HttpResponse("<h1>the first person is amir</h1>")


def home_page(rq):
    return render(rq,"for_home/first_index.html")



def second_per(rq):
    return HttpResponse("<h1> the second person is reza</h1>")
