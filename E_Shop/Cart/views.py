from django.shortcuts import render,redirect
from Accounts.models import User
from Products.models import Products
from .models import Cart

from django.contrib import messages


from django.db.models import Q

# Create your views here.

# For Searching ans multipal--------------------------------------
def Add_To_Cart(request,id):
    user=request.user
    if user.is_authenticated:
        pro=Products.objects.get(id=id)
        if pro:
            if Cart.objects.filter(Q(user=user) & Q(products=pro)).exists():
                messages.success(request, "Products is already exist in your Cart.")
                return redirect('home')
            else:
                add_cart = Cart(user=user, products=pro)
                add_cart.save()
    return  redirect('home')

def ajax_add_review(request,id):
    a_user=request.user
    pro=Products.objects.get(id=id)
    
    
        
        
    
    
    


