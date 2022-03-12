from django.shortcuts import render,redirect
from .forms import RegistrationForms


# Create your views here.
def register(request):
    form = RegistrationForms()
    if request.method == 'POST':
        form = RegistrationForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            form = RegistrationForms()
            
    else:
        return render(request, 'register/register.html',{'form':form} )
        