from django.urls import path
from . import views
urlpatterns=[



    path('', views.home),
    path('home/', views.home),
    path('about', views.about),
    path('contactus', views.contactus),
    path('services', views.services),
    path('myorders', views.myorders),
    path('myprofile', views.myprofile),
    path('product', views.prod),
    path('signup', views.login),
    path('signin', views.signin),
    path('viewdetails', views.viewdetails),
    path('process', views.process),
    path('logout', views.logout),
    path('cart', views.cart),
    path('base', views.base),
    path('admin', views.admin),

    path('sviewspurchase/', views.sviewspurchase),
    path('sprofile/', views.sprofile),
    path('sitems/', views.sitems),
    path('sindex', views.sindex),
    path('sadditems/', views.sadditems),

    path('saddcategory/', views.saddcategory),
    path('sorder/', views.s_order),
    path('siteamsdetails/', views.siteamsdetails),
    path('scategory/', views.scategory),
    path('user/signup',views.user_register,name="usersignup"),
    path('add/item',views.saler_add_item,name="saleradditem"),
    path('add/category', views.saler_add_category, name="saleraddcategory"),
    path('contact', views.contact, name="contact"),
    path('user/logindata',views.user_login,name="user_login"),
    path('user/deletecategory/<str:id>',views.delete_category,name="delete_category"),
    path('user/deleteiteam/<str:id>',views.delete_iteam,name="delete_iteam"),
    path('user/edititeam/<str:ids>',views.edit_iteam,name="edit_iteam"),
    path('user/cart/<str:ids>',views.cart,name="cart"),
    path('user/myorders/<str:ids>',views.myorders,name="myorders"),
    path('user/sorder/<str:ids>',views.s_order,name="s_order"),
    # path('logou',views.user_login,name="user_login")

]
