from django.urls import path
from .views import *
from comment.views import index as index_comment


app_name='edit'

urlpatterns = [
    
   
    path('<int:id>', edit.as_view(), name='edit'),

    
]
