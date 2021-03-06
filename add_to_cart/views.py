from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

# from .models import AddToCart
from django.views.decorators.csrf import csrf_exempt

from PayTm import Checksum
from dynamicnav.models import AbstractPainting
from django.db.models import Case, When
from .models import Orders, OrderUpdate
import json
import razorpay


# MERCHANT_KEY = 'AE#KdScA6nKrrthk'


#
# @login_required
# def cart(request):
#     if request.method == 'POST':
#         user = request.user
#         i_id = request.POST['i_id']
#         addto = AddToCart.objects.filter(user=user)
#         for i in addto:
#             if i_id == i.i_id:
#                 message = "Item added more than once to the cart"
#                 break
#         else:
#             cart = AddToCart(user=user, i_id=i_id)
#             cart.save()
#             message = "Item is successfully added"
#
#         AbstractPainting.objects.filter(painting_id=i_id).first()
#         painting = AbstractPainting.objects.all()
#         return render(request, "basic.html", {'painting': painting})
#
#     pl = AddToCart.objects.filter(user=request.user)
#     ids = []
#     for i in pl:
#         ids.append(i.i_id)
#
#     preserved = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(ids)])
#     painting = AbstractPainting.objects.filter(painting_id__in=ids).order_by(preserved)
#     return render(request, "add_to_cart/cart.html", {'painting': painting})
#

def cart(request):
    if request.method == 'POST':
        items_json = request.POST.get('itemsJson')
        first_name = request.POST.get('first_name')
        print(items_json)
        amount = 400
        print(amount)

        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip_code = request.POST.get('zip_code')
        print(zip_code)
        phone = request.POST.get('phone')
        print(first_name)
        client = razorpay.Client(auth=("rzp_test_fbGFKVWvWz5khu", "GDQzJNZt3jq126oRSKTS7Jgf"))
        payment = client.order.create({'amount': amount, 'currency': 'INR',
                                       'payment_capture': '1'})

        order = Order(items_json=items_json, first_name=first_name, last_name=last_name, email=email, address=address,
                      city=city, state=state, zip_code=zip_code, phone=phone, amount=amount, order_id=payment['id'])
        order.save()

        return render(request, 'add_to_cart/cart.html', )

    return render(request, "add_to_cart/cart.html")


@csrf_exempt
def handlerequest(request):
    if request.method == "POST":
        a = (request.POST)
        order_id = ""
        for key, val in a.items():
            if key == "razorpay_order_id":
                order_id = val
                break

        # user = Order.objects.filter(order_id=order_id).first()
        # user.paid = True
        # user.save()

    # # # paytm will send you post request here
    form = request.POST
    response_dict = {}
    for i in form.keys():
        response_dict[i] = form[i]

    #
    # verify = Checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
    # if verify:
    #     if response_dict['RESPCODE'] == '01':
    #         print('order successful')
    #     else:
    #         print('order was not successful because' + response_dict['RESPMSG'])

    return render(request, "add_to_cart/paymentstatus.html", {'response': response_dict})


#
#
def yourorders(request):
    if request.method == 'POST':
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')

        try:
            order = Order.objects.filter(order_id=orderId, email=email)
            if len(order) > 0:
                update = OrderUpdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps([updates, order[0].items_json], default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{}')

        except Exception as e:
            return HttpResponse('{}')
    return render(request, "add_to_cart/yourorders.html")
