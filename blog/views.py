import datetime
from urllib import request
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from datetime import datetime
from blog.forms import ArtikelForm
from blog.models import Artikel

# Create your views here.


def index(request):
    
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    articles = Artikel.objects.all().values()
    response = {'articles': articles}
    return render(request, 'articles.html', response)

@login_required(login_url="register/login")
def add_forum(request):
    form = []
    if not request.user.is_superuser:
        return HttpResponseRedirect('../')
        
    
    form = ArtikelForm(request.POST)
    if form.is_valid():
        new_forum = form.save(commit=False)
    
        
        
        new_forum.created_at = datetime.now().strftime("%A, %d %B %Y, %I:%M %p")
        new_forum.username = request.user.username
        
        new_forum.save()
        return HttpResponseRedirect('../')

    context = {'form' : form}
    return render(request, 'artikel_form.html', context)

