from django.db import models
from api.models.lorongmodel import Lorong
from api.models.usermodel import User

class PaymentList(models.Model):
   payment_id = models.AutoField(primary_key=True)
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   datetime = models.DateTimeField(auto_now_add=True)
   amount = models.DecimalField(max_digits=10, decimal_places=2)
   status = models.CharField(max_length=20)
   img_url = models.CharField(max_length=255)
   lorong = models.ForeignKey(Lorong, on_delete=models.CASCADE)

   def __str__(self):
      return str(self.payment_id)