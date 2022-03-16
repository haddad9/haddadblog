
from django import forms
from django.contrib.auth import  login, authenticate
from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.models import User

class RegistrationForms(UserCreationForm):
   
    firstname = forms.CharField()
   
    
    
    class Meta:
        model = User
        fields = ['firstname', 'username','password1','password2']
        
    def __init__(self, *args, **kwargs):
        super(RegistrationForms, self).__init__(*args, **kwargs)

        self.fields['firstname'].label = "Fullname"
        
        self.fields["firstname"].widget.attrs.update(
            {"placeholder": "Fullname", "autofocus": None}
        )

       
        self.fields["username"].widget.attrs.update(
            {"placeholder": "Username"}
        )
        self.fields["password1"].widget.attrs.update(
            {"placeholder": "Password"}
        )
        self.fields["password2"].widget.attrs.update(
            {"placeholder": "Confirmation Password"}
        )

        for name, field in self.fields.items():
            field.widget.attrs["required"] = None
        