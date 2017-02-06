from django.shortcuts import render,render_to_response
from forms import SignUpForm,UserLoginForm
from django.contrib.auth.models import User
from models import UserProfile
from buddy.models import Task, Assignment
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate,login,\
                                get_user_model,logout

# User Dashboard 
@login_required
def profile(request):
    users = get_user_model().objects.filter(is_staff=False)
    if request.user.is_superuser:
        tasks = Task.objects.filter(manager=request.user)
    else:
        tasks = Task.objects.filter(assignments__buddy=request.user)
        assignments = Assignment.objects.filter(buddy=request.user)
    return render(request,'home.html',{'users': users, 'tasks': tasks})


# Make a login here
def login_view(request):
    if request.method=="POST":
        form=UserLoginForm(request.POST or None)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            user=authenticate(username=username,password=password)
            login(request,user)
            return HttpResponseRedirect('/profile/')
    else:
        form=UserLoginForm()
    return render(request,'login.html',{'form':form})          

# Logout
@login_required
def user_logout(request):
    try :
        logout(request)
        return HttpResponseRedirect('/')
    except : 
        return HttpResponse("something went wrong")

# Create a New Account
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if not form.is_valid():
            return render(request, 'signup.html', {'form': form})
        else: 
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            djangouser = User(username=username)
            djangouser.set_password(password)
            djangouser.email = email 
            try:
                djangouser.save()
            except Exception as e:
                form = SignUpForm()
                return render(request,'signup.html',{'form':form})

            new_user=UserProfile()
            user = authenticate(username=username, password=password)
            ## user has been added to the current session
            new_user.user = djangouser
            new_user.save()
                    
            login(request, user)

            return HttpResponseRedirect('/')
    else:
        return render(request, 'signup.html', {'form': SignUpForm()})
