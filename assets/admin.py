from django.contrib import admin

from .models import Asset, Components, Sectors

admin.site.register(Asset)
admin.site.register(Components)
admin.site.register(Sectors)
