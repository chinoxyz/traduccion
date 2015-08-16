from django.contrib.auth import login, authenticate, logout
from django.core.urlresolvers import reverse
from django.forms.forms import NON_FIELD_ERRORS
from django.http.response import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView

from .forms import LoginForm, RegisterForm


__author__ = 'josegregorio'





class LoginView(APIView):
    follow = '/'
    def get(self, request):
        context = {'form': LoginForm()}
        return render(request, 'user/login.html', context)
    def post(self, request):
        form = LoginForm(request.data)
        if form.is_valid():
            login_data = form.cleaned_data
            user = authenticate(username=login_data['username'], password=login_data['password'])
            if user and user.is_active:
                login(request, user)
                return HttpResponseRedirect(self.follow)
            else:
                form.add_error(None, 'The username or password you entered are invalid.')
        context = {'form': form}
        return render(request, 'user/login.html', context)
        

class RegisterView(APIView):
    follow = '/'
    def get(self, request):
        context = {'form': RegisterForm()}
        return render(request, 'user/register.html', context)
    
    def post(self, request):
        form = RegisterForm(request.data)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(self.follow)
            
        context = {'form': form}
        return render(request, 'user/login.html', context)
        
        

class LogoutView(APIView):
    follow = '/'
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(self.follow)
    def post(self,request):
        return self.get(request)

def password_reset(request):
    return HttpResponse("The password reset view is coming soon...")