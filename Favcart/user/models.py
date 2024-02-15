from django.db import models


# Create your models here.
class User(models.Model):
  name = models.CharField(max_length=255,null="true")
  email = models.CharField(max_length=255,null="true")
  password = models.CharField(max_length=255,null="true")
  cpassword = models.CharField(max_length=255, null="true")
  address = models.CharField(max_length=255,null="true")
  dob = models.CharField(max_length=255,null="true")
  gender = models.CharField(max_length=255,null="true")
  role = models.CharField(max_length=255, null="true")
  contact = models.CharField(max_length=255, null="true")
  ppic = models.ImageField(upload_to='static/profile', default="")
  created_at = models.CharField(max_length=255,null="true")
  updated_at = models.CharField(max_length=255,null="true")



  class Meta:
      db_table = 'users'

class Category(models.Model):
  category=models.TextField(null="true")
  created_at = models.CharField(max_length=255, null="true")

  class Meta:
      db_table = 'category'

class Item(models.Model):
    iteamname = models.CharField(max_length=150, null="true")
    category = models.CharField(max_length=100, null="true")
    price = models.CharField(max_length=100, null="true")
    disprice = models.CharField(max_length=100, null="true")
    description = models.TextField(null="true")
    ppic = models.ImageField(upload_to='static/products', default="")
    created_at = models.CharField(max_length=255, null="true")
    updated_at = models.CharField(max_length=255, null="true")
    seller_id= models.CharField(max_length=255, null="true")
    class Meta:
      db_table = 'item'

class Contact(models.Model):
    Name=models.CharField(max_length=100,null="true")
    Email=models.CharField(max_length=120,null="true")
    Mobile=models.CharField(max_length=20,null="true")
    Message=models.TextField(null="true")

    class Meta:
      db_table = 'contact'


class addtocart(models.Model):
    pid = models.IntegerField()
    userid = models.EmailField(max_length=100)
    status = models.BooleanField()
    cdate = models.DateField()

    class Meta:
      db_table = 'addtocart'


class order(models.Model):
    pid = models.IntegerField()
    userid = models.EmailField(max_length=100)
    remarks = models.CharField(max_length=40)
    status = models.BooleanField()
    odate = models.DateField()

    class Meta:
      db_table = 'order'

class admin(models.Model):
  name = models.CharField(max_length=255,null="true")
  email = models.CharField(max_length=255,null="true")
  password = models.CharField(max_length=255,null="true")
  cpassword = models.CharField(max_length=255, null="true")
  address = models.CharField(max_length=255,null="true")
  dob = models.CharField(max_length=255,null="true")
  gender = models.CharField(max_length=255,null="true")
  role = models.CharField(max_length=255, null="true")
  contact = models.CharField(max_length=255, null="true")
  ppic = models.ImageField(upload_to='static/profile', default="")
  created_at = models.CharField(max_length=255,null="true")
  updated_at = models.CharField(max_length=255,null="true")



  class Meta:
      db_table = 'admin'