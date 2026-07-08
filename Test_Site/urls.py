"""
URL configuration for Test_Site project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
# below line for good and perfect programing for add and better sort path from each path in each app
# with this line you can write your purpose path from all app but you should make one urls.py file in you purpose app
# and write this :
#         from django.urls import path
#
#
#
#         from part_one.views import first_per, second_per, home_page
#
#         urlpatterns = [
#             path(your purpose address ,your purpose view),

#         ]

from django.urls import path,include
# i write below line of this code just for setting part from Test_Site
from . import settings
# i do not know why i import the static from the django.conf.urls.static but i import it from on my learning video
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("onepiece/",include("part_one.urls"))
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
# up line just I can say it is for upload some file in my site anyd just it
