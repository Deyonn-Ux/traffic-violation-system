
from django.urls import path
from .views import payment_checkout, payment_list

urlpatterns = [
    path('', payment_list, name='payment_list'),
    path('checkout/', payment_checkout, name='payment_checkout'),
]
