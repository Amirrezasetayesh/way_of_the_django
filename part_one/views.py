from django.shortcuts import render,HttpResponse

# Create your views here.



def first_per(rq):
    return HttpResponse("<h1>the first person is amir</h1>")

# HttpResponse just return some html code to persons like below code
def home_page(rq):
    return render(rq,"home.html")

# render is for your models and it can show some html pages to persons
# render receives one rq (the rq of your def) and one location for you html file from the templates

def second_per(rq):
    return HttpResponse("<h1> the second person is reza</h1>")
