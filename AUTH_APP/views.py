from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,logout,authenticate
from django.views import View

class Signup_view(View):
    def get(self,request):
        template_name='AUTH_APP/signup.html'
        form=UserCreationForm()
        context={'form':form}
        return render(request,template_name,context)
    
    def post(self,request):
        template_name='AUTH_APP/signup.html'
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signin_url')
        context={'form':form}
        return render(request,template_name,context)
    
class Login_view(View):
    def get(self,request):
        template_name='AUTH_APP/login.html'
        context={}
        return render(request,template_name,context)
    
    def post(self,request):
        template_name='AUTH_APP/login.html'
        un=request.POST.get('un')
        pw=request.POST.get('pw')
        User=authenticate(username=un,password=pw)
        if User:
            login(request,User)
            return redirect('show_url')
        context={}
        return render(request,template_name,context)
    
class Delete_view(View):
    def get(self,request):
        logout(request)
        return redirect('signin_url')

