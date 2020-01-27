
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
# Email
from django.core.mail import BadHeaderError, EmailMessage, send_mail

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
            
            #id = d['userinfo']['id']
            #request.session['id'] = id
            #request.session['username'] = d['userinfo']['username']
            user = user_form.save(commit=False)
            print(user.username)
            
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            login(request,user)
            if 'profile_pic' in request.FILES:
                print('found the picture!')
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
        else:
            if d['status']==0:
                return HttpResponse("your must enter the correct moodle related info -> student Id and password!!!!")
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
                myobj = {'username': studentID,'password':password}
                r = requests.post('http://157.245.126.159/api/login.php', data = myobj)
                d=r.json()
                if d['status']==1:
                    id=d['userinfo']['id']
                    request.session['id'] = id
                    request.session['username'] = d['userinfo']['username'] 
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given, please register frist!")
    else:
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
def pointlist(request):
    if request.session.get('id'):
        return render(request,'points/pointlist.html')
        

    
def game(request):
    myobj = {'user_id': '1',"points":5}
    id=request.session['id']
    r = requests.get('http://157.245.126.159/api/cut_user_points.php?user_id='+id+'&points=5', data = myobj)
    d=r.json()
    return render(request,'points/game.html')
    
def getmypoint(request):
    myobj = {'user_id': '1'}
    id=request.session['id']
    r = requests.get('http://157.245.126.159/api/get_user_points.php?user_id='+id, data = myobj)
    return HttpResponse(r)
    
def ajaxpointlist(request): 
    id=request.session['id']
    r = requests.get('http://157.245.126.159/api/get_user_pointlist.php?user_id='+id)
    return HttpResponse(r)
 
