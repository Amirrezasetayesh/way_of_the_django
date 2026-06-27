from django.urls import path



from part_one.views import first_per, second_per, home_page

urlpatterns = [
    path("person_one/",first_per),
    path("person_tow/",second_per),
    path("home_please/",home_page)
]
