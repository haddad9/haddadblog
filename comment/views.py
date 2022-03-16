
from datetime import datetime
from django.http import response
from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt


from django.contrib.auth.models import User
from .models import Comment,Artikel
from .forms import CommentForm
from django.http.response import HttpResponseNotFound, HttpResponseRedirect
from django.http.response import HttpResponse
from django.core import serializers
# There is no local timezone support, you need to know your timezone
import pytz
utc = pytz.timezone('UTC')
localtz = pytz.timezone('Asia/Jakarta')






# Create your views here.
def index(request, id):
    artikels = Artikel.objects.all().values()
    form = CommentForm(request.POST or None )

    
    response={}

    if request.method == "POST":
        if (form.is_valid):
            print(form.is_valid)
            print(form.is_valid())
            add_comment = form.save(commit=False)
            add_comment.forum = Artikel.objects.get(pk=id)

            add_comment.comment_creator =  request.user
            add_comment.forum_creator =  Artikel.objects.get(pk=id)
            add_comment.forum_creator_username = add_comment.forum_creator.username
            add_comment.id_forum = add_comment.forum_creator.pk
            add_comment.id_user = request.user.username
            add_comment.comment_creator_username = add_comment.comment_creator.username
                      
            
            time_stamp = datetime.utcnow()
            utctime = utc.localize(time_stamp)
            time_stamp_jakarta = localtz.normalize(utctime.astimezone(localtz))
            time_stamp_jakarta =time_stamp_jakarta.strftime("%A, %d %B %Y, %I:%M %p")
            add_comment.created_at = time_stamp_jakarta
            add_comment.save()
            response['form'] = form
           
            return HttpResponseRedirect(request.path_info )
    response['form'] = form
    Comment.forum_creator = Artikel.objects.get(pk = id)
    
   
    
   
    response['forum'] = Comment.forum_creator
  


    comments = Comment.objects.filter(id_forum=id)
    response['comments'] = {'comments': comments}
    print(response)
    return render(request,  "comment_list.html", response)


def delete(request,id):
    
    record = Comment.objects.get(id=id)
    record.delete()
    return render(request,  "articles.html")


def edit(request,id):
    if request.method =='POST': 
        record = Comment.objects.get(id=id)
        record.delete()
        return render(request,  "articles.html")
    return render(request,  "articles.html")

