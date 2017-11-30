from django.shortcuts import redirect

def login_redirect(request):
    return redirect('/accounts/login')

def home_redirect(request):
    return redirect('/accounts')