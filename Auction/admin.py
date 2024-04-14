from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(UserProfile)
admin.site.register(Payment)
admin.site.register(Products)
admin.site.register(Cart)
admin.site.register(Customer)
admin.site.register(auction)
admin.site.register(Bid)
admin.site.register(Notification)
admin.site.register(Wishlist)