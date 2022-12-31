from django.urls import path
from app2.views import *

app_name='gowtham2'

urlpatterns = [
    path('intro/',intro,name='intro')
]
