from django.shortcuts import render, HttpResponseRedirect, redirect
from django.urls import reverse
from django.contrib import messages

from django.contrib.auth.models import User
from register.models import UserProfile
from App_Order.models import Order, Cart
from App_Payment.forms import BillingAddress
from App_Payment.forms import BillingForm


from django.contrib.auth.decorators import login_required


import requests
from sslcommerz_python.payment import SSLCSession
from decimal import Decimal
import socket
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@login_required
def checkout(request):
    saved_address = BillingAddress.objects.get_or_create(user=request.user)
    saved_address = saved_address[0]
    print(saved_address)
    form = BillingForm(instance=saved_address)
    if request.method == "POST":
        form = BillingForm(request.POST, instance=saved_address)
        if form.is_valid():
            form.save()
            form = BillingForm(instance=saved_address)
            messages.success(request, f"Shipping Address Saved!")
    order_qs = Order.objects.filter(user=request.user, ordered=False)

    order_items = order_qs[0].orderitems.all()
    
    order_total = order_qs[0].get_totals()
    return render(request, 'App_Payment/checkout.html', context={"form":form, "order_items":order_items, "order_total":order_total, "saved_address":saved_address})

@login_required
def payment(request):
    saved_address = BillingAddress.objects.get_or_create(user=request.user)
    saved_address = saved_address[0]
    if not saved_address.is_fully_filled():
        messages.info(request, f"Please complete shipping address!")
        return redirect("App_Payment:checkout")

    #if not request.user.profile.is_fully_filled():
        #messages.info(request, f"Please complete profile details!")
        #return redirect("App_Login:profile")

    store_id = 'none5e026730bdf7f'
    API_key = 'none5e026730bdf7f@ssl'
    mypayment = SSLCSession(sslc_is_sandbox=True, sslc_store_id=store_id, sslc_store_pass=API_key)

    status_url = request.build_absolute_uri(reverse("App_Payment:complete"))
    #print(status_url)
    mypayment.set_urls(success_url=status_url, fail_url=status_url, cancel_url=status_url, ipn_url=status_url)

    order_qs = Order.objects.filter(user=request.user, ordered=False)
    order_items = order_qs[0].orderitems.all()
    order_items_count = order_qs[0].orderitems.count()
    order_total = order_qs[0].get_totals()

    mypayment.set_product_integration(total_amount=Decimal(order_total), currency='BDT', product_category='Mixed', product_name=order_items, num_of_item=order_items_count, shipping_method='Courier', product_profile='None')


    current_user = request.user
    mypayment.set_customer_info(name=current_user.first_name, email=current_user.email, address1='Bashundhara R/A', address2='sasa', city='Dhaka', postcode='1221', country='Bangladesh', phone='0120120120')

    mypayment.set_shipping_info(shipping_to=current_user.first_name, address='Bashundhara R/A', city='Dhaka', postcode='1221', country='Dhaka')


    response_data = mypayment.init_payment()
    return redirect(response_data['GatewayPageURL'])
@csrf_exempt
def complete(request):
    if request.method == 'POST' or request.method == 'post':
        payment_data = request.POST
        status = payment_data['status']

        if status == 'VALID':
            val_id = payment_data['val_id']
            tran_id = payment_data['tran_id']
            messages.success(request,f"Your Payment Completed Successfully! Your item will be delivered within 7 days!")
            return HttpResponseRedirect(reverse("App_Payment:purchase", kwargs={'val_id':val_id, 'tran_id':tran_id},))
        elif status == 'FAILED':
            messages.warning(request, f"Your Payment Failed! Please Try Again! Page will be redirected!")

    return render(request, "App_Payment/complete.html", context={})

@login_required
def purchase(request, val_id, tran_id):
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    order = order_qs[0]
    orderId = tran_id
    order.ordered = True
    order.orderId = orderId
    order.paymentId = val_id
    order.save()
    cart_items = Cart.objects.filter(user=request.user, purchased=False)
    for item in cart_items:
        item.purchased = True
        item.save()
    return HttpResponseRedirect(reverse("App_Shop:home"))

@login_required
def order_view(request):
    try:
        orders = Order.objects.filter(user=request.user, ordered=True)
        context = {"orders": orders}
    except:
        messages.warning(request, "You do no have an active order")
        return redired("App_Shop:home")
    return render(request, "App_Payment/order.html", context)
