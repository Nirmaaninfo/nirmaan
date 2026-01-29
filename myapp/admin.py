from django.contrib import admin
from .models import Category, Location, Vendor, VendorPhoto,SubCategory

admin.site.register(Category)
admin.site.register(Location)
admin.site.register(Vendor)
admin.site.register(VendorPhoto)
admin.site.register(SubCategory)