from django.shortcuts import render,HttpResponse,redirect
from AdminModule.models import Category,Product,Users,Cart
from django.core.mail import send_mail

SECRET_KEY = "OnlineStore123"
def Displaycategory():
    cats = Category.objects.all()
    return cats
    
def master(request):
    cats =Displaycategory()
    prds = Product.objects.all()
    try:
        user_checking = Users.objects.get(email_id=request.session["Username"])
        request.session['user'] = user_checking.firstname
    except:
        pass
    if("Username" in request.session):
        carts = Cart.objects.filter(email_id=request.session["Username"])
        request.session['cart_value']=len(carts)
    return render(request,'master.html',{'cats':cats,'prds':prds})

def DisplayProduct(request,id):
    cats =Displaycategory()
    prds =Product.objects.filter(category=id)
    return render(request,'DisplayProduct.html',{'cats':cats,'prds':prds})

def ViewDetails(request,id):
    cats =Displaycategory()
    prd = Product.objects.get(id=id)
    return render(request,"Viewdetails.html",{'cats':cats,'prd':prd})    

def login(request):
    if(request.method=="GET"):
        cats =Displaycategory()
        return render(request,"login.html",{'cats':cats})
    else:
        Email = request.POST["Email"]
        Password = request.POST["Password"]
        try:
            email_checking = Users.objects.get(email_id=Email,password=Password)
            request.session['Username']=Email
            return redirect(master)
        except:
            cats =Displaycategory()
            return render(request,"login.html",{"error":"Please Enter Correct Login Details",'cats':cats})


def register(request):
    if(request.method=="GET"):
        cats =Displaycategory()
        return render(request,"register.html",{'cats':cats})
    else:
        FirstName= request.POST["FirstName"]
        LastName =request.POST["LastName"]
        Password = request.POST["Password"]
        ConfirmPassword = request.POST["ConfirmPassword"]
        Email = request.POST["Email"]
        Address =  request.POST["Address"]
        Phone_number= request.POST["Phone_number"]
        if(Password==ConfirmPassword):
            try:
                email_checking = Users.objects.get(email_id=Email)
                return render(request,"register.html",{"error":"Email-id Already Register"})
            except:
                u1 = Users()
                u1.firstname = FirstName
                u1.lastname =LastName
                u1.password = Password
                u1.email_id=Email
                u1.phone_number=Phone_number
                u1.address = Address
                u1.save()
                send_mail("Hi "+FirstName+" Thank you for registering to Our Website. ", "Thank you for signin to Online Store \n Username= "+Email+"\n Password= "+Password+"\n All @Copyrights reversed", "djangoproject764@gmail.com", [Email])

        else:
            return render(request,"register.html",{"error":"Password Not Same"})
    return redirect(login)

def logout(request):
    del request.session['Username']
    return redirect(master)

def account(request):
    if("Username" in request.session):
        cats =Displaycategory()
        user = Users.objects.get(email_id=request.session["Username"])
        return render(request,"account.html",{"user":user,'cats':cats})
    else:
        return redirect(login)

def ChangePassword(request):
    if(request.method=="GET"):
        if("Username" in request.session):
            cats =Displaycategory()
            return render(request,"changepassword.html",{'cats':cats})
        else:
            return redirect(login)
    else:
        Password=request.POST["Password"]
        ConfirmPassword=request.POST["ConfirmPassword"]
        if(Password==ConfirmPassword):
            user = Users.objects.get(email_id=request.session["Username"])
            user.password=Password
            user.save()
            return redirect(account)
        else:
            cats =Displaycategory()
            return render(request,"changepassword.html",{"error":"Password Not Same",'cats':cats})
            
def addtocart(request):
    if(request.method=="POST"):
        if("Username" in request.session):
            cats =Displaycategory()
            id =request.POST["id"]
            product_name = request.POST["product_name"]
            product_price = request.POST["product_price"]
            product_category = request.POST["product_category"]
            email = request.session["Username"]
            qty = request.POST["qty"]
            try:
                email_product_checking = Cart.objects.get(email_id=email,product_id=id)
                prd = Product.objects.get(id=id)
                return render(request,"Viewdetails.html",{'cats':cats,"error":"Product already in your cart",'prd':prd})
            except:
                c = Cart()
                c.product_id = id
                c.product_name= product_name
                c.product_price=product_price
                c.email_id=email
                c.quantity=qty
                c.category=product_category
                c.save()
                return redirect(showcart)        
        else:
            return redirect(login)
        
def showcart(request):
    if(request.method=="GET"):
        if("Username" in request.session):
            cats =Displaycategory()
            carts = Cart.objects.filter(email_id=request.session["Username"])
            request.session['cart_value']=len(carts)
            total=0
            for cart in carts:
                total = total + int(cart.product_price)*int(cart.quantity)
            request.session['total']=total
            return render(request,"cart.html",{'cats':cats,"carts":carts})
        else:
            return redirect(login)

def removefromcart(request,id):
    if(request.method=="GET"):
        if("Username" in request.session):
            cats =Displaycategory()
            carts_delete = Cart.objects.get(email_id=request.session["Username"],product_id=id)
            carts_delete.delete()
            carts = Cart.objects.filter(email_id=request.session["Username"])
            request.session['cart_value']=len(carts)
            total=0
            for cart in carts:
                total = total + int(cart.product_price)*int(cart.quantity)
            request.session['total']=total
            return redirect(showcart)
        else:
            return redirect(login)

def forgotpassword(request):
    if(request.method=="GET"):
        cats =Displaycategory()
        return render(request,"forgotpassword.html",{'cats':cats})
    else:
        email = request.POST["Email"]
        try:
            email_checking = Users.objects.get(email_id=email)
            Password = email_checking.password
            Email = email_checking.email_id
            FirstName = email_checking.firstname
            send_mail("Hi "+FirstName+" Your Login Details ", "Login Details \n Username= "+Email+"\n Password= "+Password+"\n All @Copyrights reversed", "djangoproject764@gmail.com", [email])
            return redirect(login)
        except:
            cats =Displaycategory()
            return render(request,"forgotpassword.html",{"error":"Your Email is not register",'cats':cats})

def ContactUs(request):
    if(request.method=="GET"):
        cats =Displaycategory()
        return render(request,"contactus.html",{'cats':cats})
    else:
        name = request.POST["Name"]
        email = request.POST["Email"]
        phone_number = request.POST["PhoneNumber"]
        message = request.POST["Message"]
        return HttpResponse(message)
        