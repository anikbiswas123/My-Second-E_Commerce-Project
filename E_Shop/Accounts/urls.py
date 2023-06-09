from django.urls import path
from .views import *

urlpatterns = [
    path('customer_reg/', customer_reg, name='customer_reg'),
    path('seller_reg/', seller_reg, name='seller_reg'),
    path('seller_info/', seller_info, name='seller_info'),


    path('user_login/', user_login, name='user_login'),
    path('user_logout/', user_logout, name='user_logout'),
    
    path('user_profile/', user_profile, name='user_profile'),
    path('email-change/', email_change, name='email_change'),
    path('customer_address/', customer_address, name='customer_address'),

    path('seller_profile/', seller_profile, name='seller_profile'),



    path('otp_verify/', otp_verify, name='otp_verify'),
    path('resend_OTP/', resend_OTP, name='resend_OTP'),



    path('forger-password-email/', Take_Email, name='Take_Email'),
    path('forger-password-otp/', Take_OTP, name='Take_OTP'),
    path('forger-password-set/', Take_New_Password, name='Take_New_Password'),
]