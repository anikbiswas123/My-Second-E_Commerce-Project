from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(productReview)

@admin.register(Cart)
class cartadmin(admin.ModelAdmin):
    list_display=('creation_date','user','products','quantity','total')
    
    


