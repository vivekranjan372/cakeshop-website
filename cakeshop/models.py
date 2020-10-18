from django.db import models
from django.forms import ModelForm,Textarea


# Create your models here.

class Registration(models.Model):
 name=models.CharField(max_length=100)
 email=models.CharField(max_length=100)
 password=models.CharField(max_length=100)
 mobile=models.CharField(max_length=100)
 confirm_password=models.CharField(max_length=100)

 class Meta:
  db_table="test_register"



class SellCake(models.Model):
 cake_name=models.CharField(max_length=100)
 cake_image=models.ImageField(upload_to='static/images',default="")
 cake_price=models.CharField(max_length=100,default="")
 cake_description=models.CharField(max_length=100)
 cake_ingredients=models.CharField(max_length=100)
 cake_method=models.CharField(max_length=100)
 uploader_id=models.CharField(max_length=100,default="")
 class Meta:
  db_table="cake_details"


class RegisterUser(models.Model):
 name=models.CharField(max_length=30)
 email=models.EmailField(max_length=20)
 password=models.CharField(max_length=30)
 mobile=models.CharField(max_length=12)
 address=models.CharField(max_length=100)
 items=models.CharField(max_length=30,default="")
 class Meta:
  db_table="cake_user"



class SellAndBuy(models.Model):
 first_name=models.CharField(max_length=30)
 last_name=models.CharField(max_length=30)
 locality=models.CharField(max_length=30)
 street=models.CharField(max_length=30)
 city=models.CharField(max_length=30)
 pin_code=models.CharField(max_length=30)
 state=models.CharField(max_length=30)
 country=models.CharField(max_length=30)
 email=models.EmailField(max_length=30)
 mobile=models.CharField(max_length=30)

 payment_method=models.CharField(max_length=100,default="")
 delivery_status=models.CharField(max_length=100,default="")
 user_type=models.CharField(max_length=20,default="")
 cake_price=models.CharField(max_length=50,default="")
 class Meta:
  db_table="user_all_details"

class AddItem(models.Model):
 cake_name=models.CharField(max_length=100)
 cake_image = models.CharField(max_length=100)
 cake_price = models.CharField(max_length=100)
 addedUser = models.EmailField(max_length=100)
 class Meta:
  db_table="add_to_cart"








