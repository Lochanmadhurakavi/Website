from django.shortcuts import render, redirect
from .models import Article
from .forms import FormArticle, RegisterUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages



# Create your views here.

@login_required(login_url='login')
def home(request): 
    form1 = FormArticle()
    if request.method == 'POST':
        form = FormArticle(request.POST)
        if form.is_valid():
            saving = form.save()
            data = Article.objects.get(id=saving.id)
        return render(request,  'article/home.html', {'form1':form1, 'data':data})
    context = {'form1':form1}
    return render(request, 'article/home.html', context)


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.success(request, ("There was an error logging In, Try Again.."))
            return redirect('login')
    
    else:
        context = {}
        return render(request, 'article/login.html', context)

def logout_user(request):
    logout(request)
    messages.success(request, ("You were logged out"))
    return redirect('login')

def register_user(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password = password)
            login(request, user)
            messages.success(request, ('Registration successful'))
            return redirect('login')
    else:
        form = RegisterUserForm()

    context = {'form':form}
    return render(request, 'article/register_user.html', context)




