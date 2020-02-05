from django.contrib import admin
from .models import Product
from .models import Offer
from .models import kids


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','price','stock')

admin.site.register(Product,ProductAdmin)

# class HomeAdmin(admin.ModelAdmin):
#     list_display = ('category','image_url')
#
# admin.site.register(Home,HomeAdmin)

class OfferAdmin(admin.ModelAdmin):
    list_display = ('name','price','stock')

admin.site.register(Offer,OfferAdmin)

class kidsAdmin(admin.ModelAdmin):
    list_display = ('name','price','stock')

admin.site.register(kids,kidsAdmin)

