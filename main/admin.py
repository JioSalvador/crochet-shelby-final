from django.contrib import admin
from . models import MyUser, Product, Order, Cart, CartItem, OrderItem

admin.site.register(MyUser)

admin.site.register(Product)

admin.site.register(Order)

admin.site.register(OrderItem)

admin.site.register(Cart)

admin.site.register(CartItem)


