from django.urls import path

from . import views

urlpatterns = [
  path('', views.viewmissions, name='viewmissions'),
  path('<int:mission_id>', views.process_query, name='json_example'),
  path('data', views.radiopie2, name='radiopie2'),
  path('<int:mission_id>', views.viewtransmissiondata, name='viewtransmissiondata'),
  path('dbquery', views.dbquery, name='dbquery'),
]