from django.contrib import admin
from .models import *
# Registering models
admin.site.register(customer)
admin.site.register(product)
admin.site.register(seller)
admin.site.register(soldproduct)
