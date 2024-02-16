from django.contrib import admin
from .models import MenuItem, MenuImage, MenuReview, Order

admin.site.register(MenuItem)
admin.site.register(MenuImage)
admin.site.register(MenuReview)
admin.site.register(Order)
