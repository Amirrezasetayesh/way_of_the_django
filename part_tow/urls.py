from django.urls import path

from . import views

urlpatterns = [
path("choices/",views.check_choices,name="choices"),
path("select_this/",views.select,name="select_character"),
path("not_select_this/",views.not_select,name="not_select_character"),
path("select_again/",views.select_again,name="select_again_character"),

]
