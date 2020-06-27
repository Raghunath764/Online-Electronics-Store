from django.db import models

class Category(models.Model):
    cname = models.CharField(max_length=30)

    def __str__(self):
        return self.cname

    class Meta:
        db_table = 'Category'

class Product(models.Model):
    pname = models.CharField(max_length=30)
    price = models.FloatField(default=200)
    description = models.CharField(max_length=100)
    imageurl = models.ImageField(upload_to='images/',default='abc.jpg')
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    class Meta:
        db_table = 'Product'
    
class Users(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    password =models.CharField(max_length=30)
    email_id = models.CharField(max_length=40)
    phone_number = models.CharField(max_length=10)
    address = models.CharField(max_length=200)

    class Meta:
        db_table = 'Users'

class Cart(models.Model):
    product_id = models.CharField(max_length=30)
    product_name = models.CharField(max_length=30)
    product_price= models.FloatField(default=200)
    quantity = models.FloatField(default=200)
    email_id = models.CharField(max_length=40)
    category = models.CharField(max_length=40)

    class Meta:
        db_table = "Cart"





