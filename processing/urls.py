from django.urls import path

from . import views

urlpatterns = [
  path('', views.upload, name='ingest'),
  # path('<int:asset_id>', views.asset, name='asset'),
  # path('search', views.search, name='search'),
]