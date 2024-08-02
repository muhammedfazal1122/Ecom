from django.contrib import admin

# Register your models here.
from Product.models import Product,Variation,Image



admin.site.register(Product)
admin.site.register(Variation)
admin.site.register(Image)
