from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from water_selling.models import *
import uuid,random
from django.contrib.auth import logout

transaction_id = 0
# Create your views here.

def index(request):
    return render(request, "index.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/")

def products_details(request):
    prod_obj = product.objects.all()
    context = {"prod_obj": prod_obj}

    return render(request, "products.html", context)


def displayCart(request):
    cart_list = []
    customre_no = request.user.id
    cart_obj = cart.objects.filter(cart_customer_id=customre_no)
    for i in cart_obj:
        prod_id = i.cart_product_id
        prod_details = product.objects.get(product_id=prod_id)
        prod_count =  i.cart_product_quantity
        cart_list.append((prod_details,prod_count))
    context = {"cart_list": cart_list}
    return render(request, "cart.html", context)


def addtoCart(request, value):
    prod_obj = product.objects.all()
    context = {"prod_obj": prod_obj}
    customre_no = request.user.id
    cart_obj = cart.objects.all()
    for i in cart_obj:
        if i.cart_customer_id == customre_no and i.cart_product_id == value:
            i.cart_product_quantity += 1
            i.save()
            return render(request, "products.html", context)   
    cart_obj = cart(cart_customer_id=customre_no, cart_product_id=value, cart_product_quantity=1)
    cart_obj.save()
    return render(request, "products.html", context)

def emptyCart(request):
    customre_no = request.user.id
    cart_obj = cart.objects.filter(cart_customer_id=customre_no)
    for i in cart_obj:
        i.delete()
    return HttpResponseRedirect("/products/")

def checkout_view(request):
    prod_list = []
    customre_no = request.user.id
    cart_obj = cart.objects.filter(cart_customer_id=customre_no)
    total_price = 0
    for i in cart_obj:
        prod_id = i.cart_product_id
        prod_details = product.objects.get(product_id=prod_id)
        prod_count =  i.cart_product_quantity
        total_price += prod_details.product_price * prod_count 
        prod_list.append((prod_details,prod_count))
    total_price = total_price * 0.8
    context = {"cart_obj": prod_list, "total_price": total_price}
    return render(request, "checkout.html", context)

def checkout_success(request):
    data = request.POST
    customer_id = request.user.id
    cutomer_name = data.get("name")
    customer_email = data.get("email")
    customer_address = data.get("address") 
    customer_city = data.get("city")
    customer_zip = data.get("zip")
    customer_contact = data.get("contact")

    customer_obj = customer(customer_id=customer_id, customer_name=cutomer_name, customer_email=customer_email, customer_address=customer_address, customer_city=customer_city, customer_zipcode=customer_zip, customer_contact=customer_contact)
    customer_obj.save()

    prod_list = []
    cart_obj = cart.objects.filter(cart_customer_id=customer_id)
    total_price = 0
    for i in cart_obj:
        prod_id = i.cart_product_id
        prod_details = product.objects.get(product_id=prod_id)
        prod_count =  i.cart_product_quantity
        total_price += prod_details.product_price * prod_count
        prod_list.append((prod_details,prod_count))
    context = {"cart_obj": prod_list, "total_price": total_price}

    return render(request, "order.html",context)

def place_order(request):
    curr_cust_id = request.user.id
    customer_id = customer.objects.get(customer_id=curr_cust_id)
    cart_obj = cart.objects.filter(cart_customer_id=customer_id.customer_id)
    total_ammt = 0
    total_quantity = 0
    ord_id = random.randint(65,100000)
    for i in cart_obj:
        pid = product.objects.get(product_id=i.cart_product_id)
        p_quan = i.cart_product_quantity
        total_quantity += p_quan
        total_ammt += pid.product_price * p_quan
        ord_obj = orders(order_id=ord_id    , order_customer_id=customer_id, order_product_id=pid, order_quantity=p_quan)
        ord_obj.save()
        i.delete()
    
    transaction_id = random.randint(1,10000000)
    transaction_obj = transaction(transaction_id=transaction_id, transaction_customer_id=customer_id,transaction_order_id = ord_id ,transaction_total=total_ammt)
    transaction_obj.save()

    cur_transac_id = transaction.objects.filter(transaction_customer_id=customer_id.customer_id)
    for i in cur_transac_id:
        if i.transaction_id == transaction_id:
            cur_transac_id = i
            break
    delivery_id = random.randint(34,10000000) 
    delivery_obj = delivery(delivery_id = delivery_id,delivery_customer_id = customer_id,delivery_order_id = ord_id ,
        delivery_transaction_id = cur_transac_id, 
        delivery_city = customer_id.customer_city, 
        delivery_address = customer_id.customer_address, 
        delivery_zipcode = customer_id.customer_zipcode, 
        delivery_contact = customer_id.customer_contact)
    delivery_obj.save()
    

    return render(request,"thankyou.html")


def my_orders(request):
    curr_cust_id = request.user.id
    customer_id = customer.objects.get(customer_id=curr_cust_id)
    order_obj = orders.objects.filter(order_customer_id=customer_id.customer_id).order_by('-order_date')
    order_list = []
    for i in order_obj:
        product_list = product.objects.get(product_id=i.order_product_id_id)
        order_list.append((i,product_list))
    context = {"order_list": order_list}
    return render(request, "my_orders.html", context)

