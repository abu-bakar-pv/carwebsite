from django.contrib import admin
from buggy_app.models import Car, Color,Brand,Customer,Booking,Times


admin.site.register(Color)
admin.site.register(Car)
admin.site.register(Customer)
admin.site.register(Brand)
admin.site.register(Booking)
admin.site.register(Times)
