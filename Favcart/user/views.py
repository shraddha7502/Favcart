import os

from dask.bag import Item

from django.contrib import messages
from django.contrib.messages import constants
from django.shortcuts import render, redirect

from django.http import HttpResponse,HttpResponseRedirect
from .models import *

from datetime import date, datetime
from django.db import connection
# Create your views here.
def dictfetchall(cursor):
    desc=cursor.description
    return [
            dict(zip([col[0] for col in desc],row))
            for row in cursor.fetchall()
          ]
def about(request):
    return render(request,'user/about.html')

def cart(request):
    return render(request,'user/cart.html')

def contactus(request):
    return render(request,'user/contactus.html')

def home(request):
    id = request.session.get('user_id')
    email = request.session.get('user_email')
    mobile = request.session.get('user_mobile')
    name = request.session.get('user_name')
    itemdata = Item.objects.all()
    cdata = Category.objects.all()
    if id is not None:



        items = {
            'name': name,
            'email': email,
            'mobile': mobile,
            'item': itemdata,
            'category': cdata
        }
        return render(request,'user/index.html',items)
    else:
        items = {
            'item': itemdata,
            'category': cdata
        }
        return render(request, 'user/index.html', items)

def signin(request):
    return render(request,'user/login.html')

def user_login(request):
    if request.method=='POST':
        email = request.POST.get('email')
        password =request.POST.get('passwd')

        check= User.objects.filter(email=email).filter(password=password)
        # print(check.query)
        if check:
            # role=check[0]['role']
            for n in check:
                role=n.role
                id = n.id
                name = n.name
                email = n.email
                contact = n.contact
                # print(role)
                if role=='1':
                    request.session['user_id'] = id
                    request.session['user_name'] = name
                    request.session['user_email'] = email
                    request.session['user_mobile'] = contact

                    request.session.set_expiry(7200)
                    # data = {
                    #     'adminsettings': settingss,
                    #     'msgflash': 'successfully Login ' + user.username
                    # }
                    # print(data)
                    return HttpResponseRedirect('/home/')

                if role=='2':
                    request.session['seller_id'] = id
                    request.session['seller_name'] = name
                    request.session['seller_email'] = email
                    request.session['seller_mobile'] = contact

                    request.session.set_expiry(7200)
                    return HttpResponseRedirect('/sindex')


                else:
                    return HttpResponse( "<script>alert('this is worng userid and password  ....');window.location.href='/signin'</script>")



        else:
                return HttpResponse("<script>alert('this is worng userid and password  ....');window.location.href='/signin'</script>")

def logout(request):
    request.session.flush()
    request.session.clear_expired()
    return HttpResponseRedirect('/')





def myorders(request):
    return render(request,'user/myorders.html')

def myprofile(request):
    return render(request,'user/myprofile.html')

# def process(request):
    # return render(request,'user/process.html')

def prod(request):
    return render(request,'user/product.html')

def services(request):
    return render(request,'user/services.html')

def login(request):
    return render(request,'user/signup.html')

def viewdetails(request):
    a = request.GET.get('msg')
    data = Item.objects.filter(id=a)
    data={
        "d": data,
    }

    return render(request,'user/viesdetails.html', data)


# def viewdetails(request):
#     return render(request, 'user/viewdetails.html')



def base(request):
    return render(request,'base.html')

def sprofile(request):
    return render(request,'seller/sprofile.html')

def sviewspurchase(request):
    return render(request,'seller/sviewspurchase.html')

def sitems(request):
    id = request.session.get('seller_id')
    email = request.session.get('seller_email')
    mobile = request.session.get('seller_mobile')
    name = request.session.get('seller_name')
    if id is not None:
        itemdata = Item.objects.filter(seller_id=id)

        data={
            'name': name,
            'email': email,
            'mobile': mobile,
            'item':itemdata
        }

        return render(request,'seller/sitems.html',data)

def sindex(request):
    id = request.session.get('seller_id')
    email = request.session.get('seller_email')
    mobile = request.session.get('seller_mobile')
    name = request.session.get('seller_name')
    # print(id)
    if id is not None:
        itemdata = Item.objects.filter(seller_id=id)
        totalcategory=itemdata.count()
        itemcategory = Category.objects.all()
        totaliteam = itemcategory.count()
        # cursor = connection.cursor()
        # cursor.execute("SELECT o.*,p.* FROM `order` o,item p where o.pid=p.id and p.seller_id='" + str(id) + "'")
        # totalordera = cursor.fetchall()
        # print(orderdata)
        # itemorder=order.objects.filter(userid=id)
        # totalorder=itemorder.count()
        orderdata = order.objects.filter(id=id)
        totalorder = orderdata.count()


        print(totalorder)
        category = {
            'name':name,
            'email':email,
            'mobile':mobile,
            'category': itemcategory,
            'item': itemdata,
            'totaliteam': totaliteam,
            'totalcategory':totalcategory,
            'totalorder':totalorder,
        }
        return render(request,'seller/sindex.html',category)
    else:
        return HttpResponseRedirect('/')

def sadditems(request):
    return render(request,'seller/sadditems.html')

def saddcategory(request):

    return render(request,'seller/saddcategory.html')

def sorder(request):

    return render(request,'seller/sorder.html')

def admin(request):

    return render(request,'admin/aindex.html')

def siteamsdetails(request):
    id = request.session.get('seller_id')
    email = request.session.get('seller_email')
    mobile = request.session.get('seller_mobile')
    name = request.session.get('seller_name')
    # print(id)
    if id is not None:
        itemdetails={
            'name': name,
            'email': email,
            'mobile': mobile,

        }
    return render(request,'seller/siteamsdetails.html',itemdetails)

def scategory(request):
    id = request.session.get('seller_id')
    email = request.session.get('seller_email')
    mobile = request.session.get('seller_mobile')
    name = request.session.get('seller_name')
    # print(id)
    if id is not None:
        itemcategory = Category.objects.all()
        totaliteam=itemcategory.count()

        category = {
            'name': name,
            'email': email,
            'mobile': mobile,
            'category': itemcategory,
            'totaliteam': totaliteam,
        }
        return render(request,'seller/scategory.html',category)

def user_register(request):
    if request.method=='POST':
        name = request.POST.get('name')
        email =request.POST.get('email')
        passwd = request.POST.get('passwd')
        cpassword = request.POST.get('cpassword')
        address = request.POST.get('address')
        dob = request.POST.get('dob')
        gender = request.POST.get('gender')
        roles= request.POST.get('role')
        mobile=request.POST.get('mobile')
        if len(request.FILES)!=0:
           ppic=request.FILES['fu']

        users = User(name =name ,email=email,password=passwd,cpassword=cpassword,address=address,dob=dob,gender=gender,role=roles,contact=mobile,ppic=ppic)
        users.save()
        return HttpResponse("<script>alert('Registertion successfull ....');window.location.href='/signin'</script>")
        # else:
        # users = User(name=name, email=email, password=passwd, cpassword=cpassword, address=address, dob=dob,gender=gender, role=roles, contact=mobile, ppic=ppic)
        # users.save()
        # return HttpResponse("<script>alert('Registertion successfull ....');window.location.href='/signin'</script>")
        #








def saler_add_item(request):
    id = request.session.get('seller_id')
    # print(id)
    if id is not None:
        if request.method=='POST':
            today = date.today()
            Iteamname = request.POST.get('iteamname')

            price = request.POST.get('price')
            disprice = request.POST.get('disprice')
            category = request.POST.get('category')
            description=request.POST.get('description')
            if len(request.FILES) != 0:
                ppic = request.FILES['image']
            item= Item(iteamname=Iteamname,price=price,disprice=disprice,category=category,description=description,ppic=ppic,created_at=today,seller_id=id)
            item.save()
            return HttpResponse("<script>alert('Iteam add successfuly ....');window.location.href='/sindex'</script>")
            # return HttpResponseRedirect('/sindex')
    else:

        return HttpResponseRedirect('/')

def saler_add_category(request):
    id = request.session.get('seller_id')
    # print(id)
    if id is not None:
        if request.method=='POST':
            categoryname = request.POST.get('category')
            today = date.today()


            category = Category( category=categoryname,created_at=today)
            category.save()
            return HttpResponse("<script>alert('category add successfuly ....');window.location.href='/sindex'</script>")
            # return HttpResponseRedirect('/sindex')
    else:
            return HttpResponseRedirect('/')


def contact(request):
    userid = request.session.get('user_id')
    email = request.session.get('user_email')
    mobile = request.session.get('user_mobile')
    name = request.session.get('user_name')


    if request.method=='POST':
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        message = request.POST.get('message')

        contact=Contact(Name=name,Mobile=mobile,Email=email,Message=message)
        contact.save()
    ite = {
        'name': name,
        'email': email,
        'mobile': mobile,
        'userid': userid,

    }

    return render(request,'user/contactus.html',ite)




def delete_category(request,id):
    category=Category.objects.filter(id=id)
    category.delete()
    return HttpResponse("<script>alert('category deleted successfuly ....');window.location.href='/user/scategory'</script>")
    # return HttpResponseRedirect('/')

def delete_iteam(request,id):
    category=Item.objects.filter(id=id)
    category.delete()
    return HttpResponse("<script>alert('iteam deleted successfuly ....');window.location.href='/user/sitems/'</script>")

def edit_iteam(request,ids):
    id = request.session.get('seller_id')
    email = request.session.get('seller_email')
    mobile = request.session.get('seller_mobile')
    name = request.session.get('seller_name')
    # print(id)
    if id is not None:
        iteam=Item.objects.filter(id=ids)
        itemcategory = Category.objects.all()
        if request.method =='POST':
            iteam.today = date.today()
            iteam.iteamname = request.POST.get('iteamname')

            iteam.price = request.POST.get('price')
            iteam.disprice = request.POST.get('disprice')
            iteam.category = request.POST.get('category')
            iteam.description = request.POST.get('description')
            if len(request.FILES) != 0:
                if len(iteam.ppic)>0:
                    os.remove(iteam.ppic.path)
                iteam.ppic = request.FILES['image']


                iteam.save()
            # else:
            #
            #     # item = Item(iteamname=Iteamname, price=price, disprice=disprice, category=category,
            #     #             description=description, updated_at=today)
                iteam.today = date.today()
                iteam.Iteamname = request.POST.get('iteamname')

                iteam.price = request.POST.get('price')
                iteam.disprice = request.POST.get('disprice')
                iteam.category = request.POST.get('category')
                iteam.description = request.POST.get('description')
                iteam.save()
            messages.success(request,"iteam update sussfully")
            return HttpResponseRedirect('/user/sitems/')
        # print(iteam)
        edit={
            'name': name,
            'email': email,
            'mobile': mobile,
            'iteam':iteam,
            'category':itemcategory,
        }
        return render(request, 'seller/siteamsdetails.html',edit )


def process(request):
    userid=request.session.get('user_id')
    pid=request.GET.get('pid')
    btn=request.GET.get('bn')
    # print(btn)
    if userid is not None :
        if btn=='cart':
            checkcartitem=addtocart.objects.filter(pid=pid,userid=userid)
            if checkcartitem.count()==0:

               addtocart(pid=pid,userid=userid,status=True,cdate=datetime.now()).save()
               return HttpResponse("<script>alert('your iteam is successfuly addded in cart');window.location.href='/cart'</script>")

            else:
                 return HttpResponse ("<script>alert('this iteam is already enterd..');window.location.href='/user/home/'</script>")

        elif btn=='order':
             order(pid=pid,userid=userid,remarks="panding",status=True,odate=datetime.now()).save()
             return HttpResponse("<script>alert('your order have confird...');window.location.href='myorders'</script>")


        elif btn=='orderfromcart':
             res=addtocart.objects.filter(pid=pid,userid=userid)
             res.delete()
             order(pid=pid,userid=userid,remarks="panding",status=True,odate=datetime.now()).save()
             return HttpResponse("<script>alert('your order have confirmd...');window.location.href='myorders'</script>")
        return render(request, 'user/process.html', {"alreadylogin": True})
    else:
          return HttpResponse("<script>alert('First you log in ....');window.location.href='/signin'</script>")



def cart(request):
    if request.session.get('user_id'):
       userid=request.session.get('user_id')
       email = request.session.get('user_email')
       mobile = request.session.get('user_mobile')
       name = request.session.get('user_name')
       cursor=connection.cursor()
       cursor.execute("SELECT item.*,addtocart.status AS cartstatus FROM `addtocart`, item WHERE   item.id=addtocart.pid && addtocart.`userid`="+str(userid))
       cartdata=dictfetchall(cursor)
       pid=request.GET.get('pid')
       if request.GET.get('pid'):
           res=addtocart.objects.filter(pid=pid,userid=userid)
           res.delete()
           return HttpResponse( "<script>alert('your product have been remove successfully...');window.location.href='/cart'</script>")
       # print(cartdata)
       edit = {
           'name': name,
           'email': email,
           'mobile': mobile,
           'cart': cartdata,

       }
       return render(request, 'user/cart.html', edit)
    else:
          return HttpResponse("<script>alert('First you log in ....');window.location.href='/signin'</script>")




def myorders(request):
    if request.session.get('user_id'):

        userid=request.session.get('user_id')
        email = request.session.get('user_email')
        mobile = request.session.get('user_mobile')
        name = request.session.get('user_name')
        oid=request.GET.get('oid')
        orderdata=""
        if userid:
            cursor=connection.cursor()
            cursor.execute("SELECT o.*,p.* FROM `order` o,item p where o.pid=p.id and o.userid='"+str(userid)+"'")
            orderdata=cursor.fetchall()
            # print(orderdata)
        if oid:
              result=order.objects.filter(pid=oid,userid=userid)
              result.delete()
              return  HttpResponse("<script>alert('your iteam has been cancelled.');window.location.href='/myorders'</script>")

        return render(request,'user/myorders.html',{"pendingorder":orderdata,"name":name,})
    else:
          return HttpResponse("<script>alert('First you log in ....');window.location.href='/signin'</script>")


def prod(request):
    userid = request.session.get('user_id')
    email = request.session.get('user_email')
    mobile = request.session.get('user_mobile')
    name = request.session.get('user_name')

    cdata=Category.objects.all().order_by('-id')
    x=request.GET.get('abc')
    pdata=""
    if x is not None :
        pdata= Item.objects.filter(category=x)
    else:
        pdata = Item.objects.all().order_by('-id')

    return render(request,'user/product.html',{"cat":cdata,"products":pdata,"name":name,})



# def s_order(request,ids):
#     id = request.session.get('seller_id')
#     email = request.session.get('seller_email')
#     mobile = request.session.get('seller_mobile')
#     name = request.session.get('seller_name')
#     print(id)
#     if id is not None:
#         itemdetails={
#             'name': name,
#             'email': email,
#             'mobile': mobile,
#
#         }
#     return render(request,'seller/sorder.html',itemdetails)


def s_order(request):
    id = request.session.get('seller_id')
    email = request.session.get('seller_email')
    mobile = request.session.get('seller_mobile')
    name = request.session.get('seller_name')
    # print(id)
    # print(name)
    if id is not None:
        # itemcategory = Category.objects.all()
        # totaliteam=itemcategory.count()
        orderdata = ""

        cursor = connection.cursor()
        cursor.execute("SELECT o.*,p.* FROM `order` o,item p where o.pid=p.id and p.seller_id='" + str(id) + "'")
        orderdata = cursor.fetchall()
            # print(orderdata)
        category = {
            'name': name,
            'email': email,
            'mobile': mobile,
            'pendingorder':orderdata,
            # 'category': itemcategory,
            # 'totaliteam': totaliteam,
        }
        return render(request,'seller/sorder.html',category)