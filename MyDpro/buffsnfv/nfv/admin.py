from django.contrib import admin

from .models import Interfaces, Instances, Images

admin.site.register(Interfaces)
admin.site.register(Instances)
admin.site.register(Images)
# Register your models here.
