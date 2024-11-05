from django.urls import path,include
from .views import *

urlpatterns =[
    path('postdata/',dataListCreateView.as_view(), name='postdata'),
]