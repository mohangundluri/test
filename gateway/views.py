from django.shortcuts import redirect, render
from .forms import PaymentForm
import razorpay
from .models import PaymentModel

razorpay_key_id = "rzp_test_dXoF5LUpycLixy"
razorpay_key_secret = "LYiDEcTlt5AHnnbqoAimgEyA"
def home(request):
    
    if request.method == "POST":
        name = request.POST["name"]
        amount = int(request.POST["amount"]) * 100
    
        # Creating razorpay client
        client = razorpay.Client(auth = (razorpay_key_id, razorpay_key_secret))
        
        # Create order payment
        payment_response = client.order.create(data = dict(amount = amount, currency = 'INR'))
        
        form = PaymentForm(request.POST)
        
        
        order_id = payment_response['id']
        order_status =payment_response["status"]
        
        if order_status == "created":
            PaymentModel.objects.create(name= name, amount = amount, order_id = order_id).save()
            return render(request, 'gateway/home.html', {'form':form,'payment_response':payment_response})
    
    form = PaymentForm()
    return render(request, 'gateway/home.html', {'form':form})


def payment_status(request):
    if request.method == 'POST':
        response = request.POST
        
        param_dict = {
            'razorpay_order_id': response['razorpay_order_id'],
            'razorpay_payment_id': response['razorpay_payment_id'],
            'razorpay_signature': response['razorpay_signature']
        }
        
        client = razorpay.Client(auth = (razorpay_key_id, razorpay_key_secret))
        
        try:
            status = client.utility.verify_payment_signature(param_dict)
            payment = PaymentModel.objects.get(order_id = response['razorpay_order_id'])
            payment.razorpay_payment_id = response['razorpay_payment_id']
            payment.paid = True
            payment.save()
            return render(request, 'gateway/payment_status.html', {'status': True})
        except:
            return render(request, 'gateway/payment_status.html', {'status': False})
