from django.urls import path
from .views import *
from comment.views import index as index_comment

urlpatterns = [
    path('', index, name = 'index'),
    path('add/', add_forum, name='add'),
   
    path('<int:id>', index_comment, name='comment'),
]
