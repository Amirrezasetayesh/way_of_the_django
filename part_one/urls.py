from django.urls import path



from part_one.views import first_per, second_per, main_page,gran_line,login_user,logout_user

urlpatterns = [
    path("main_page/",main_page,name="main_page"),
    path("grand_line/",gran_line,name="grand_line"),
    path("login/",login_user,name="login_user_site"),
    path("logout/",logout_user,name="logout_user_site")
#     you chose one name for you url and then you can use this name in html cods like below code:
#     {% url 'name of your Selected url ' %}
]
