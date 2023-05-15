from django.contrib import admin

from .models import Category, Topping, Wrapper, IceCream


admin.site.register([Category, Topping, Wrapper, IceCream])
