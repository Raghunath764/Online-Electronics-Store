from django.urls import path
from UserApp import views

urlpatterns = [
    path('home/',views.master),
    path('DisplayProduct/<id>',views.DisplayProduct),
    path('ViewDetails/<id>',views.ViewDetails),
    path('login/',views.login),   
    path('register/',views.register),   
    path('logout/',views.logout),   
    path('account/',views.account),  
    path('ChangePassword/',views.ChangePassword),
    path('addtocart/',views.addtocart),
    path('showcart/',views.showcart),
    path('removefromcart/<id>',views.removefromcart),
    path('forgotpassword/',views.forgotpassword),
    path('ContactUs',views.ContactUs),
]