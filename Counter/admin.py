from django.contrib import admin

# Register your models here.
from .models import driver
from .models import autobus
from .models import counter
from .models import page

class driveradmin(admin.ModelAdmin):
    list_display = ['__unicode__', 'bus']
    class Meta:
        model = driver
admin.site.register(driver, driveradmin)

class counteradmin(admin.ModelAdmin):
    list_display = ['bus', 'kilometrage']
    class Meta:
        model = counter
    list_filter = ['datetime']
admin.site.register(counter, counteradmin)

admin.site.register(autobus)


class pageadmin(admin.ModelAdmin):
    list_display=['title', 'content', 'alias']
    class Meta:
        model = page
admin.site.register(page, pageadmin)