from django.contrib import admin
from .models import Category,Product,Users,Cart

class ProductAdmin(admin.ModelAdmin):
    list_display=['id','pname','price','description','imageurl','category']

class CategoryAdmin(admin.ModelAdmin):
    list_display=['id','cname']

class UsersAdmin(admin.ModelAdmin):
    list_display=['firstname','lastname','password','email_id','phone_number','address']

class CartAdmin(admin.ModelAdmin):
    list_display= ['product_id','product_name','product_price','quantity','email_id','category']

admin.site.register(Product,ProductAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Users,UsersAdmin)
admin.site.register(Cart,CartAdmin)

