from django.forms import Form, CharField
from django.forms.models import ModelForm
from django.forms.widgets import TextInput, PasswordInput, EmailInput

from .models import AppUser
from django.db import transaction
from django.contrib.auth.models import User
class LoginForm(Form):
    ATTR_DICT = {'class': 'form-control'}
    username = CharField(label='Email', widget=TextInput(attrs=ATTR_DICT))
    password = CharField(label='Password', widget=PasswordInput(attrs=ATTR_DICT))
    error_css_class = 'error'
    

class RegisterForm(ModelForm):
    
    class Meta:
        model = AppUser
        fields = ['first_name', 'last_name', 'email']
    
    password = CharField(label='Password', widget=PasswordInput())
    error_css_class = 'error'
    
    @transaction.atomic
    def save(self, commit=True, *args, **kwargs):
        data = self.cleaned_data
        credential = User.objects.create_user(username=data.get("email"), password=data.get("password"))
        
        user = super(RegisterForm, self).save(commit = False, *args, **kwargs)
        user.credential=credential
        if(commit):
            user.save()
            
        return user
        
        #data = self.cleaned_data;"""