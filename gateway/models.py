from django.db import models


class PaymentModel(models.Model):
    
    name = models.CharField(max_length=50)
    amount = models.CharField(max_length=50)
    order_id = models.CharField(max_length=100, blank= True)
    razorpay_payment_id = models.CharField(max_length=100,blank= True )
    paid = models.BooleanField(default=False)
    
    def __str__(self):
        
        return f"{self.name} {self.amount} "
    
