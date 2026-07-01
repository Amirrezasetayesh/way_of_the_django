
from django.db import models






class Person(models.Model):

    First_name=models.CharField(max_length=20)

    Last_name=models.CharField(max_length=20)

    Gender=models.CharField(max_length=5)

    Height=models.CharField()

    Weight=models.CharField()

    Age=models.IntegerField(blank=True,null=True)
    # about blank if blank is true you can write nothing in you field
    # about null if null is true so you can write none in filed
    Phone_number=models.CharField(blank=True,null=True)

    Email=models.EmailField(max_length=80,blank=True,null=True)

    User_Name=models.CharField(max_length=20,blank=True,null=True)



    def __str__(self):
        return f"{self.First_name} {self.Last_name}"
# if you write the def str in you models so you can see your method you chose in return (self.any_method) in the admin table

class Personal_data(models.Model):

    Home_address=models.CharField(blank=True,null=True)

    Office_Address=models.CharField(blank=True,null=True)

    House_Phone=models.CharField(blank=True,null=True)

    Emai_Password=models.CharField(blank=True,null=True)

    Phone_password=models.CharField(blank=True,null=True)
#     for now
    photo_of_person=models.ImageField(upload_to="upload/photos",blank=True,null=True)
    #     this method is for save and upload the photos

    person=models.ForeignKey(Person,on_delete=models.CASCADE,default=1)
#     when you make the person then you can use all of the object of the person class like first_name or last_name
#     if on_delete is models.cascade so when you del the father model , after that child model del

    def __str__(self):
        return f"personal data of {self.person.First_name}"




