from django.urls import path
from . import views 

# /blog
urlpatterns = [
  path('',views.data_scrapping,name='data_scrapping'),
  
]