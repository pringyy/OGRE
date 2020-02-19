# HTTP
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
# Auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
import requests
from points.forms import UserForm, UserProfileInfoForm, ContactForm

import json
from django.contrib.auth.models import User
# Email
from django.core.mail import BadHeaderError, EmailMessage, send_mail
# Notifications
from django.contrib import messages

@login_required
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
    
def register(request):
    registered = False
    if request.method == 'POST':
        # we use the crispy form, which has post request
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        studentID = request.POST.get('StudentID', None)
        password = request.POST.get('password', None)
        
        #store the user password and uername, sent it via the api by post request, moodle have the auth function for it
        myobj = {'username':studentID,'password':password}
        # add the moodle RESTful api here!
        r = requests.post('http://157.245.126.159/api/login.php', data = myobj)
        #if d['status] == 1, the user is a moodle user 
        d = r.json()
        print(d['status'])
        print(studentID,password)
        
        # the status 1 indicate this user is valid in moodle
        if user_form.is_valid() and profile_form.is_valid() and d['status']==1:
            
            id=d['userinfo']['id']
            request.session['id'] = id
            request.session['username'] = d['userinfo']['username'] 
            user = user_form.save(commit=False)
            print(user.username)
            
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            messages.success(request, "Successfully Registered!")
            login(request,user)
            if 'profile_pic' in request.FILES:
                print('found the picture!')
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
        else:
            if d['status']==0:
                messages.error(request, "Enter your moodle username and password")
                #deprecate this line
                #return HttpResponse("your must enter the correct moodle related info -> student Id and password!!!!")
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
        myobj = {'username': studentID,'password':password}
        r = requests.post('http://157.245.126.159/api/login.php', data = myobj)
        d=r.json()
        user = authenticate(username=username, studentID = studentID, password=password)
        print(username,studentID,password)
        
        if user:

            if user.is_active:
                

                if d['status']==1:
                    id=d['userinfo']['id']
                    request.session['id'] = id
                    request.session['username'] = d['userinfo']['username'] 
                    messages.success(request, "Sucessfully logged in! Welcome!")
                    login(request,user)
                    return HttpResponseRedirect(reverse('index'))
                elif d['status']==0:
                    messages.error(request, "Please use your moodle password!")
                    
                
                

            else:
                messages.error(request, "Please register with your moodle account first!")
        
        elif d['status']==1:
            id=d['userinfo']['id']
            request.session['id'] = id
            request.session['username'] = d['userinfo']['username'] 
            u = User.objects.get(username=username)
            if u:
                u.set_password(password)
                u.save()
                user2 = authenticate(username=username, studentID = studentID, password=password)
                messages.success(request, "Sucessfully logged in! Welcome!")
                login(request,user2)
                return HttpResponseRedirect(reverse('index'))
            else:
                messages.error(request, "Please enter the correct username!")
                
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            messages.error(request, "Incorrect username or password!")

    return render(request, 'points/login.html', {})


def ogre_points(request):
    context_dict = {}
    return render(request, 'points/ogre_points.html', context_dict)


def about(request):
    context_dict = {}
    return render(request, 'points/about.html', context_dict)

def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_name = form.cleaned_data['contact_name']
            contact_email = form.cleaned_data['contact_email']
            subject = form.cleaned_data['subject']
            content = form.cleaned_data['content']
            message = "Name: " + contact_name + "\nEmail: " + contact_email +  "\nMessage: " + content
            email = EmailMessage(subject, message,
                                to=['contactogre2020@gmail.com']) #change to your email
            email.send()

            return redirect('../thanks/')
    return render(request, 'points/contact.html', {'form': form})

def thanks(request):
    context_dict = {}
    return render(request, 'points/thanks.html', context_dict)

def faq(request):
    context_dict = {}
    return render(request, 'points/faq.html', context_dict)

def profile(request):
    context_dict = {}
    return render(request, 'points/profile.html', context_dict)

@login_required
def get_user_profile(request, username):
    user = User.objects.get(username=username)
    return render(request, 'points/profile.html', {"user":user})

def pointlist(request):
    if request.session.get('id'):
        return render(request,'points/pointlist.html')

def game(request):
    myobj = {'user_id': '1',"points":5}
    id=request.session['id']
    r = requests.get('http://157.245.126.159/api/get_user_points.php?user_id='+id, data = myobj)
    d=r.json()
    if int(d['points']) >= 5:
        r = requests.get('http://157.245.126.159/api/cut_user_points.php?user_id='+id+'&points=5', data = myobj)
        return render(request,'points/game.html')
    else:
        messages.error(request, "You don't have enough points to play!")
        return HttpResponseRedirect(reverse('index'))

def getmypoint(request):
    myobj = {'user_id': '1'}
    id=request.session['id']
    #user.studentprofileinfo.currentPoints = 9
    r = requests.get('http://157.245.126.159/api/get_user_points.php?user_id='+id, data = myobj)
    d=r.json()
    #print(d['points'])
    return HttpResponse(r)

def iterateJSON(request):
    context_dict = {}
    return render(request, 'points/iterateJSON.html', context_dict)

def ajaxpointlist(request): 
    id=request.session['id']
    r = requests.get('http://157.245.126.159/api/get_user_pointlist.php?user_id='+id)
    return HttpResponse(r)

def pointcalculate(request):
    id=request.session['id']
    r = requests.get('http://157.245.126.159/api/get_user_pointlist.php?user_id='+id)
    d = r.json()
    point_d = d['rows']
    total_point = 0
    spent_point = 0
    #print(d['rows'])
    for i in range(len(point_d)):
        #print(point_d[i]['amount'])
        if (point_d[i]['type'] == '-'):
            spent_point += int(point_d[i]['amount'])
        else:
            total_point +=int(point_d[i]['amount'])
    d.update({'total_point':total_point})
    d.update({'spent_point':spent_point})
    
    return JsonResponse(d)


def changeUsername(request):
    # first get the session id, this user for each transaction record
    id=request.session['id']
    # get the curretn auth user
    user = request.user
    print(user.username)
    username = request.GET.get('username', None)
    
    print(username)
   
    

    if request.user.username == username:
        
        
        d = {"status":0,'message':'  Do not enter the same username!   '}
        return JsonResponse(d)
    else:
        u = User.objects.get(username=request.user.username)
        u.username = username
        u.save()
        r = requests.get('http://157.245.126.159/api/getnickname.php?user_id='+id+'&action=update&alternatename='+username)
        return HttpResponse(r)    

       
    
   
