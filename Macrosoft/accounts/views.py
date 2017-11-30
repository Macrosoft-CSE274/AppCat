from django.shortcuts import render, redirect
from accounts.forms import RegistrationForm, EditProfileForm, ApplicationSubmitForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from django.http import HttpResponse
from accounts import models

def home(request):
    numbers = {1, 2, 3, 4, 5}
    name = 'Jimmy Dudley'

    args = {'keyName': name, 'numbers': numbers}
    return render(request, 'accounts/home.html', args)

def register(request):
    if request.method =='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(request, "/accounts/login/")
    else:
        form = RegistrationForm()
        args = {'form': form}
        return render(request, 'accounts/reg_form.html', args)

def view_profile(request):
    args = {'user': request.user}
    return render(request, 'accounts/profile.html', args)

def edit_profile(request):
    print(request.user)
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        print(request.user)

        if form.is_valid():
            form.save()
            return redirect('/accounts/profile')

    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'accounts/edit_profile.html', args)

def search_page(request):

    print("searching")
    if request.method == "GET":
        keyword = request.GET.get("keyword", "")
        finalList = []
        for app in models.ApplicationEntry.objects.all():
            if keyword in app.name:
                finalList.append(app)
        args = {"appList" : finalList}
        return render(request, "accounts/searchResult.html", args)

    else:
        return HttpResponse("Something went wrong, please try again")

def app_page(request):
    print("printing")
    if request.method == "GET":
        appname = request.GET["appname"]
        print("name already get")
        list = models.ApplicationEntry.objects.all();
        app = None
        for application in list:
            if application.name == appname:
                app = application
        args = {"app" : app}

        return render(request, "accounts/app_detail_page.html", args)

    else:
        return HttpResponse("It seems something went wrong during going to the app page")

def submit_app(request):
    print("going to the app submit page\n\n")
    if request.method =='POST':
        print("go to the post mode")
        form = ApplicationSubmitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(request, "/accounts/application_submit_page.html/")
    else:
        print("go to other mode")
        form = ApplicationSubmitForm()
        args = {'form': form}
        return render(request, 'accounts/application_submit_page.html', args)









