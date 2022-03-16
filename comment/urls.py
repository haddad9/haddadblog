from django.urls import path
from .views import *
from comment.views import index as index_comment


app_name='comment'

urlpatterns = [
    
   
    path('edit/<int:id>', edit, name='edit'),
    path('<int:id>', delete, name='delete'),
    
]
