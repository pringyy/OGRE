
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
        studentID = request.POST.get('StudentID', None)
        password = request.POST.get('password', None)
        myobj = {'username':studentID,'password':password}
        # add the moodle RESTful api here!
        r = requests.post('http://157.245.126.159/api/login.php', data = myobj)
        #if d['status] == 1, the user is a moodle user 
        d = r.json()
        print(d['status'])
        print(studentID,password)
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
            messages.success(request, "Sucessfully Registered!")
            login(request,user)
            if 'profile_pic' in request.FILES:
                print('found the picture!')
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
        else:
            if d['status']==0:
                messages.error(request, "your must enter the correct moodle related info -> student Id and password!!!!")
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
                    messages.error(request, "you seems like change your moodle password, please use that password!")
                    
                
                

            else:
                messages.error(request, "Account is not active, please register via your moodle account first!")
        
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
                messages.error(request, "please enter the correct username!")
                
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            messages.error(request, "Incorrect username or password!,please register via your moodle account first!")

    return render(request, 'points/login.html', {})
def ogre_points(request):
    context_dict = {}
    return render(request, 'points/ogre_points.html', context_dict)


def about(request):
    context_dict = {}
    return render(request, 'points/about.html', context_dict)

def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_name = form.cleaned_data['contact_name']
            contact_email = form.cleaned_data['contact_email']
            subject = form.cleaned_data['subject']
            content = form.cleaned_data['content']
            try:
                email = EmailMessage(subject,
                                    content,
                                    contact_email,
                                    ['yauchungki513@gmail.com'], #change to your email
                                   )
                # send_mail(subject,
                #             content,
                #             contact_email,
                #             ['yauchungki513@gmail.com'], #change to your email
                #             )
                email.send()
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
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
        messages.error(request, "you don't have enough points to play!")
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