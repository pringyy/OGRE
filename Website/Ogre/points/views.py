
# HTTP
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse

# Auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from points.forms import UserForm, UserProfileInfoForm

def index(request):
    context_dict={}
    return render(request, 'points/index.html', context_dict)


@login_required
def show_login(request):
    return HttpResponse("Now you are logged in!")


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
    

#def user_login(request):
 #   return render(request, 'points/login.html', {'login_message': 'Please enter your username and password'})

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                print('found the picture!')
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request,'points/register.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        studentID = request.POST.get('studentID')
        password = request.POST.get('password')
        user = authenticate(username=username, studentID = studentID, password=password)
        print(username,studentID,password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            #åreturn HttpResponse("Invalid login details given, please register frist!")
            #return render(request, 'points/login.html', {})
            toastr.error('I do not think that word means what you think it means.', 'Inconceivable!')

    else:
        return render(request, 'points/login.html', {})
def ogre_points(request):
    context_dict = {}
    return render(request, 'points/ogre_points.html', context_dict)


def about(request):
    context_dict = {}
    return render(request, 'points/about.html', context_dict)

def contact(request):
    context_dict = {}
    return render(request, 'points/contact.html', context_dict)

def faq(request):
    context_dict = {}
    return render(request, 'points/faq.html', context_dict)


def profile(request):
    context_dict = {}
    return render(request, 'points/profile.html', context_dict)
