from django.contrib import admin

from .models import Asset, Component, Sector

class AssetAdmin(admin.ModelAdmin):
  list_display = ('id', 'partnumber', 'serialnumber', 'cbp_component', 'cbp_sector', 'cost')
  list_display_links = ('id', 'partnumber')
  list_filter = ('cbp_component', 'cbp_sector')
  search_fields = ('partnumber', 'cost', 'description')

admin.site.register(Asset, AssetAdmin)
admin.site.register(Component)
admin.site.register(Sector)
