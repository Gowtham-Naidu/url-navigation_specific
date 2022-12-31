from django.urls import path
from app1.views import *

app_name='rock1'

urlpatterns=[
    
    path('intro/',intro,name='intro')
]