from django.contrib import admin
from water_selling.models import *

admin.site.register(employee)
admin.site.register(customer)
admin.site.register(product)
admin.site.register(delivery)
admin.site.register(transaction)
admin.site.register(cart)
admin.site.register(orders)