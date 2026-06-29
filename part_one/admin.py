from django.contrib import admin
from .models import Person,Personal_data

# Register your models here.

admin.site.register(Person)

admin.site.register(Personal_data)


#  if you want save and working you model in you site so you should write below code:
# from .models import model_name
# admin.site.register(model_name)