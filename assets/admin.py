from django.contrib import admin

from .models import Asset, Component, Sector

class AssetAdmin(admin.ModelAdmin):
  list_display = ('id', 'partnumber', 'serialnumber', 'component', 'sector', 'cost')
  list_display_links = ('id', 'partnumber')
  list_filter = ('component', 'sector')
  search_fields = ('partnumber', 'cost', 'description')
  list_per_page = 25

admin.site.register(Asset, AssetAdmin)
admin.site.register(Component)
admin.site.register(Sector)
