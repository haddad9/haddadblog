from django.urls import include, path
from .views import *
app_name = "blog"

urlpatterns = [    
    path('', index, name='index'),
        
]


