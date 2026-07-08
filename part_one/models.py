
from django.db import models






class Character(models.Model):

    First_name=models.CharField(max_length=20)

    Last_name=models.CharField(max_length=20)

    gender_list=[("m","male"),("f","female")]
    Gender=models.CharField(choices=gender_list)

    Height=models.CharField()

    Weight=models.CharField()

    Age=models.IntegerField(blank=True,null=True)
    # about blank if blank is true you can write nothing in you field
    # about null if null is true so you can write none in filed
    Head_gift=models.CharField()
    f_or_uf=[("f","friendly"),("unf","unfriendly")]
    role_of_the_character=models.CharField(choices=f_or_uf)

    f_level_list=[("y","YOnko"),("SH","ShiJeBoKay"),("n_p","normal_pirate"),("A","AdMiArl"),("s_a","second_AdMiRal"),("n_m","normal_marian")]
    character_level=models.CharField(choices=f_level_list,default=f_level_list[-1])




    def __str__(self):
        return f"{self.First_name}"
# if you write the def str in you models so you can see your method you chose in return (self.any_method) in the admin table

class Personal_data(models.Model):

    Home_address=models.CharField(blank=True,null=True)

    Office_Address=models.CharField(blank=True,null=True)
#     for now
    photo_of_the_character=models.ImageField(upload_to="upload/photos",blank=True,null=True)
    #     this method is for save and upload the photos

    character=models.ForeignKey(Character,on_delete=models.CASCADE,default=1)
#     when you make the person then you can use all of the object of the person class like first_name or last_name
#     if on_delete is models.cascade so when you del the father model , after that child model del
#     for use the object of person for personal_data models you should write somthing like below code:
#     name of your model (the model make with personal_data).person.name of your some object from person like First_name
    def __str__(self):
        return f"personal data of {self.character.First_name}"




