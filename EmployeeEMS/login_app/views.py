from django.shortcuts import render
from django.http import HttpResponse
from login_app.forms import UserForm

# Create your views here.
def welcome(request):
    return HttpResponse("Hello from Vasu!!")

def login(request):
    form = UserForm()
    if(request.method == 'POST'):
        form = UserForm(request.POST)
        if form.is_valid():
            logged_by = form.cleaned_data['username']
            print(form.cleaned_data['username'])
            return render(request, 'login_app/login_success.html', {'logged_user':logged_by})            

    return render(request, 'login_app/index.html', {'login_form':form})

