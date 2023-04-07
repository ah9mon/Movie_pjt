
# Create your views here.
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods, require_POST, require_safe


@require_http_methods(['GET','POST'])
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('movies:index')
        
    else:
        form = AuthenticationForm()
    
    context = {
        "form" : form
    }

    return render(request, 'accounts/login.html', context)

@login_required
@require_POST
def user_logout(request):
    logout(request)
    return redirect('movies:index')

@require_http_methods(['GET','POST'])
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('movies:index')
        
    else:
        form = CustomUserCreationForm()
    
    context = {
        'form' : form,
    }

    return render(request, 'accounts/signup.html', context)

@login_required
@require_http_methods(['GET','POST'])
def update(request):
    print('>>>update')
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance = request.user)
        if form.is_valid():
            form.save()
            return redirect('movies:index')
        
    else:
        form = CustomUserChangeForm(instance = request.user)
    
    context = {
        'form' : form,
    }

    return render(request, 'accounts/update.html', context)

@login_required
@require_POST
def delete(request):
    request.user.delete()
    logout(request) 
    return redirect('movies:index')

@login_required
@require_http_methods(['GET','POST'])
def password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('movies:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form' : form ,
    }

    return render(request, 'accounts/change_password.html', context)

