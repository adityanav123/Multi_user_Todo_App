from django.shortcuts import render,redirect
from todo.views import index
from django.http import HttpResponse
# LOGIN FORM
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
# Create your views here.

def start_page(request):
    return render(request,'registration/start_page.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1'] # password1 - default
            user = authenticate(username = username, password=password) # authenticate the user automatically
            login(request, user)
            return redirect('start_page')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form' : form})