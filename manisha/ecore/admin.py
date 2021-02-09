from django.contrib import admin

# Register your models here.
from ecore.models import Marchent, Lenin, RFID

admin.site.register(Marchent)
admin.site.register(Lenin)
admin.site.register(RFID)