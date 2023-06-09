from django.db import models
from Accounts.models import User
from Products.models import Products

# Create your models here.
class Cart(models.Model):
    
    creation_date = models.DateTimeField(auto_now_add=True)


    updated = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ForeignKey(Products, on_delete=models.CASCADE)

    purchesed = models.BooleanField(default=False)

    quantity = models.PositiveIntegerField(default=1)
    total = models.FloatField(default=0.00)

    def __str__(self):
        return f"{self.products.Product_Name} X {self.quantity}"
    
    @property
    def total_price(self):
        total = self.quantity * self.products.Special_Price
        total_amount = format(total, '0.2f')
        return total_amount

class productReview(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    product=models.ForeignKey(Products,on_delete=models.SET_NULL,null=True)
    Review=models.TextField()
    rating=models.IntegerField(default=None)
    date=models.DateTimeField(auto_now_add=True)
    
    class meta:
        verbose_name_plural='Product Reviews'
    
    def __str__(self) -> str:
        return self.product.Product_name
    
    def get_Ratting(self):
        return self.rating    
    
    
