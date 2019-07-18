from django.urls import path

from . import views

urlpatterns = [
  path('', views.viewmissions, name='viewmissions'),
  # path('<int:mission_id>', views.viewtransmissiondata, name='viewtransmissiondata'),
  path('<int:mission_id>', views.radiopie, name='radiopie'),
  path('<int:mission_id>', views.viewtransmissiondata, name='viewtransmissiondata'),
  # path('search', views.search, name='search'),
]