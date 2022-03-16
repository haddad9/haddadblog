from django.urls import path,include
from .views import *
from comment.views import index as index_comment
import comment.urls as comment

urlpatterns = [
    path('', index, name = 'index'),
    path('add/', add_forum, name='add'),
   
    path('<int:id>', index_comment, name='comment'),
    path('comment/',include(comment)),
]
