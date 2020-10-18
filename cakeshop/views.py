from django.shortcuts import render,redirect
from cakeshop.models import Registration,SellCake,RegisterUser,SellAndBuy,AddItem
from django.contrib import messages
from django.db.models.query import RawQuerySet
from cakeshop import models
from django.http import HttpResponse
from django.contrib.sessions.models import Session
from django.core.files.storage import FileSystemStorage
import hashlib



# Create your views here.

def home(request):
    if request.session.has_key('is_login'):
        count = 0;
        cakeinfo = SellCake.objects.all()
        count += count + 1
        print(cakeinfo)
        print(count)
        if 'user_email' in request.session:
            current_user = request.session.get('user_email')
            return render(request, "home.html", {'cakeinfo': cakeinfo, 'current_user': current_user})
    return render(request,"home.html")
def cake_type(request):
    if request.session.has_key('is_login'):
        count = 0;
        cakeinfo = SellCake.objects.all()
        count += count + 1
        print(cakeinfo)
        print(count)
        if 'user_email' in request.session:
            current_user = request.session.get('user_email')
            return render(request, "cake_type.html", {'cakeinfo': cakeinfo, 'current_user': current_user})
    return  render(request,"cake_type.html")
def footer(request):
    return render(request,"footer.html")
def login(request):

    if request.session.has_key('is_login'):
        print("session has key")
        if 'user_email' in request.session:
           current_user=request.session.get('user_email')
           return redirect('/customer_orders/')

    if request.method=="POST":
        if request.POST['email'] and request.POST['password']:
            email=request.POST['email']
            password=request.POST['password']
            password=hashlib.sha256(password.encode())
            password=password.hexdigest()
            print(password)
            emailname="name"
            passwordname="password"
            isEmail=Registration.objects.raw('select * from cake_user where email=%s',[email])
            isPassword=Registration.objects.raw('select * from cake_user where password=%s',[password])

            for iterate in isEmail:
                emailname=iterate.id
                break
            for iterate in isPassword:
                passwordname=iterate.id
                break
            if emailname==passwordname:
               request.session['is_login']=True
               session_key=request.session.has_key('is_login')
               request.session['user_email']=email
               current_user = request.session['user_email']
               print(current_user)
               print("user matched")
               return   HttpResponse("<script type='text/javascript'>alert('you are successfully logged in');"
                                    "window.parent.location.href='/customer_orders/'</script>")

            else:
                print("not user found")
                return HttpResponse("<script type='text/javascript'>alert('your username or password is invalid');"
                                    "window.parent.location.href='/login/'</script>")


    if 'user_email' in request.session:
     current_user = request.session['user_email']
     return render(request,"user_profil.html",{'current_user':current_user})
    else:
        return render(request, "login.html")


def testimonial(request):
    return render(request,"testimonial.html")
def recipe(request,id):
       if 'user_email' in request.session:
          current_user = request.session.get('user_email')
          if id!=0:
           cake_desc = SellCake.objects.filter(id=id)
           print("yes we are in recipe")

           return render(request,"recipe.html",{'cake_desc':cake_desc,'current_user':current_user})

       return render(request,"recipe.html")
def remove_product(request,id):
    remove_item=AddItem.objects.filter(id =id)
    if 'total_amount' in request.session:
        total=request.session.get('total_amount')
        for item in remove_item:
            total=total-int(item.cake_price)
            request.session['total_amount']=total
            break
        remove_item.delete()
        return HttpResponse(
        "<script type='text/javascript'>alert('your product has removed successfully'); window.parent.location.href = '/basket/0';</script>")



def sell_cake(request):
    if request.method == "POST":
        print("data is posted")
        cake_name = request.POST['cake_name']
        cake_image = request.FILES['cake_image']
        cake_description = request.POST['cake_description']
        cake_ingredients = request.POST['cake_ingredients']
        cake_method = request.POST['cake_method']
        cake_price=request.POST['cake_price']
        save_data = SellCake()
        print(save_data)
        if cake_name and cake_image and cake_description and cake_ingredients and cake_method and cake_price:
            filesave = FileSystemStorage()
            filename = filesave.save(cake_image.name, cake_image)
            uploaded_url = filesave.url(filename)
            save_data.cake_name = cake_name
            save_data.cake_image = uploaded_url
            save_data.cake_description = cake_description
            save_data.cake_ingredients = cake_ingredients
            save_data.cake_method = cake_method
            save_data.cake_price=cake_price
            if 'user_email' in request.session:
                save_data.uploader_id = request.session.get('user_email')  # current user
            save_data.save()
            print("your cake is uploaded")
            return HttpResponse(
                "<script type='text/javascript'>alert('your cake details has uploaded successfully'); window.parent.location.href = '/';</script>")


        else:
            print("not uploaded")
    if request.session.has_key('is_login'):
        if 'user_email' in request.session:
            current_user = request.session.get('user_email')
            print("yes current user is preesent")
            return render(request, "sell_cake.html", {'current_user': current_user})

    else:
        return HttpResponse(
            "<script type='text/javascript'>alert('please login first to sell your products'); window.parent.location.href = '/login/';</script>")


    return render(request, "sell_cake.html")
def logout(request):
    if request.session.has_key('is_login'):
        print("sesion has key")
        request.session.flush()
        return HttpResponse("<script type='text/javascript'>alert('you have logged out..');"
                            "window.parent.location.href='/'</script>")
def basket(request,id):
    if request.session.has_key('is_login'):
        if 'user_email' in request.session:
            current_user=request.session.get('user_email')
            cake_detail=SellCake.objects.filter(id=id)
            addToCart=AddItem()
            for c in cake_detail:
                addToCart.cake_name=c.cake_name
                addToCart.cake_price=c.cake_price
                addToCart.cake_image=c.cake_image
                addToCart.addedUser=current_user
                addToCart.save()
                break
            query = "select * from add_to_cart where addedUser =%s";
            showItem = AddItem.objects.raw(query,[current_user])
            total=0
            for amount in showItem:
                total+=int(amount.cake_price)
            request.session['total_amount']=total
            print(total)
            print(showItem)
            return render(request, "basket.html", {'showItem': showItem, 'current_user': current_user,'total_amount':total})
    else:
        return HttpResponse(
            "<script type='text/javascript'>alert('Please login to see items in your cart..');"
            "window.parent.location.href='/login/'</script>")
    return  render(request,"basket.html")
def cerousel(request):
    return render(request,"cerousel.html")
def checkout1(request):
    if request.method=="POST":
        if 'user_email' in request.session:
            current_user=request.session.get('user_email')
            total = request.session.get('total_amount')
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            locality = request.POST['locality']
            street = request.POST['street']
            city = request.POST['city']
            pin_code = request.POST['pin_code']
            state = request.POST['state']
            email = request.POST['email']
            country = request.POST['country']
            mobile = request.POST['mobile']
            if first_name and last_name and locality and street and city and pin_code and state and email and mobile and country:
                detail=SellAndBuy.objects.filter(email=current_user)

                for saveData in detail:
                    saveData.first_name = first_name
                    saveData.last_name = last_name
                    saveData.street = street
                    saveData.locality = locality
                    saveData.city = city
                    saveData.pin_code = pin_code
                    saveData.email = email
                    saveData.mobile = mobile
                    saveData.state = state
                    saveData.country = country
                    saveData.save()
                    break

                print("all personal data has been saved")
                return redirect('/checkout3/')
    elif 'total_amount' in request.session:
                    user_email=request.session.get('user_email')
                    total = request.session.get('total_amount')
                    userAddress=SellAndBuy.objects.filter(email=user_email)
                    return render(request,"checkout1.html",{'total':total,'userAddress':userAddress})



    return render(request,"checkout1.html")
def checkout3(request):
    if request.method=="POST":
        payment=request.POST['payment']
        if 'total_amount' in request.session:
            total=request.session.get('total_amount')
            current_user=request.session.get('user_email')
            if payment:
             confirm_payment=SellAndBuy.objects.filter(email=current_user)
             for save_data in confirm_payment:
                save_data.payment_method=payment
                save_data.cake_price=total
                save_data.user_type="Buyer"
                save_data.save()
                break

        return redirect('/checkout4/')
    elif 'total_amount' in request.session:
        total = request.session.get('total_amount')
        return render(request,"checkout3.html",{'total':total})

    return render(request,"checkout3.html")
def checkout4(request):
    current_user = request.session.get('user_email')
    if request.method=="POST":
         confirm_payment = SellAndBuy.objects.filter(email=current_user)
         for placeorder in confirm_payment:
             placeorder.delivery_status="Order has been placed"
             placeorder.save()
             break
         if 'total_amount' in request.session:
             del request.session['total_amount']
         return HttpResponse("<script type='text/javascript'>alert('Thank you for purchashing with us, please visit again..');"
                             "window.parent.location.href='/'</script>")
    else:
        query = "select * from add_to_cart where addedUser =%s";
        showItem = AddItem.objects.raw(query, [current_user])
        total=request.session.get('total_amount')
        print(showItem)
        return render(request, "checkout4.html",
                      {'showItem': showItem, 'current_user': current_user, 'total': total})
    return render(request,"checkout4.html")
def customer_account(request):
    #change Password method
    if request.method=="POST":
        old_password=request.POST['old_password']
        old_password=hashlib.sha256(old_password.encode())
        old_password=old_password.hexdigest()
        new_password=request.POST['new_password']
        con_new_password=request.POST['con_new_password']
        if old_password and new_password and con_new_password:
            if 'user_email' in request.session:
                userId=request.session.get('user_email')
                editInfo=RegisterUser.objects.filter(email=userId)
                for iterate in editInfo:
                    if iterate.password==old_password:
                        print("yes old password is matched")
                        if new_password==con_new_password:
                            print("ok")
                            new_password=hashlib.sha256(new_password.encode())
                            new_password=new_password.hexdigest()
                            iterate.password=new_password
                            iterate.save()
                            return HttpResponse(
                                "<script text='text/javascript'>alert('Your Password is changed succesfully..');"
                                "window.parent.location.href='/customer_account/'</script>")
                            break
                        else:
                            return HttpResponse(
                                "<script text='text/javascript'>alert('Your current password did not match..');"
                                "window.parent.location.href='/customer_account/'</script>")
                            break

                    else:
                        return HttpResponse("<script text='text/javascript'>alert('Your Previous password did not match..');"
                                            "window.parent.location.href='/customer_account/'</script>")
                        break

                        #end of password changed
    if 'user_email' in request.session:
        current_user = request.session.get('user_email')
        return render(request, "customer_account.html", {'current_user': current_user})

    return render(request,"customer_account.html")
def customer_order(request):
    return render(request,"customer_order.html")
def customer_orders(request):
    if 'user_email' in request.session:
        current_user = request.session.get('user_email')
        return render(request, "customer_orders.html", {'current_user': current_user})
    return render(request,"login.html")
def customer_wishlist(request):
    if 'user_email' in request.session:
        current_user = request.session.get('user_email')
        return render(request, "customer_wishlist.html", {'current_user': current_user})
    return render(request,"customer_wishlist.html")
def navbar(request):
    if request.session.has_key('is_login'):
        count = 0;
        cakeinfo = SellCake.objects.all()
        count += count + 1
        print(cakeinfo)
        print(count)
        if 'user_email' in request.session:
            current_user = request.session.get('user_email')
            get_name=RegisterUser.objects.filter(email=current_user)
            return render(request, "navbar.html", {'cakeinfo': cakeinfo, 'current_user': current_user})
    return render(request,"navbar.html")
def register(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']
        password=hashlib.sha256(password.encode())
        password=password.hexdigest()
        print(password)
        if name and email and password:
            userId=SellAndBuy()
            userId.email=email
            userId.save()
            savetable=RegisterUser()
            savetable.name=name
            savetable.email=email
            savetable.password=password
            savetable.save()
            return HttpResponse("<script type='text/javascript'>alert('you have registered successfully please login');"
                                "window.parent.location.href='/login/'</script>")
    return render(request,"register.html")
def about(request):
    return render(request,"about.html")
def updateUserDetails(request):
    if request.method=="POST":
        print("update details has triggered")
        name=str(request.POST['first_name']+" "+str(request.POST['last_name']))
        email=request.POST['email']
        mobile=request.POST['mobile']
        address=str(request.POST['locality'])+","+str(request.POST['street'])+","+request.POST['city']+","+request.POST['pin_code']+","+request.POST['state']+","+request.POST['country']
        if 'user_email' in request.session:
            current_user=request.session.get('user_email')
            editDetails=RegisterUser.objects.filter(email=current_user)
            for iterate in editDetails:
                iterate.name=name
                iterate.email=email
                iterate.mobile=mobile
                iterate.address=address
                iterate.save()
                break
            return HttpResponse("<script text='text/javascript'>alert('Your Personal details have changed Successfully..');"
                                "window.parent.location.href='/customer_account/'</script>")

    return render(request,"customer_account.html")





