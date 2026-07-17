from django.urls import path



from . import views

urlpatterns = [
    path("main_page/",views.main_page,name="main_page"),
    path("grand_line/",views.gran_line,name="grand_line"),
    path("login/",views.login_user,name="login_user_site"),
    path("logout/",views.logout_user,name="logout_user_site"),
    path('signup/', views.signup_user, name='signup_user_site'),
#     you chose one name for you url and then you can use this name in html cods like below code:
#     {% url 'name of your Selected url ' %}
]
