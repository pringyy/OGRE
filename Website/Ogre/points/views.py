#THIS FILE PROVIDES THE VIEWS FOR THE WHOLE APPLICATION
#THIS FILE ALLOWS FOR REQUESTS IN THE APPLICATION
#IT IS ALSO WHERE THE API CALLS ARE MADE, IF YOU WANT TO EDIT THEM CHANGE THE APIcall.py FILE
#IF YOU WANT TO CHANGE THE COST OF CERTAIN REQUESTS THAT WILL REMOVE POINTS, EDIT THE costValues.py FILE

#HTTP imports
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
# Django Authentication imports
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
import requests
from points.forms import UserForm, UserProfileInfoForm, ContactForm
from points.models import StudentProfileInfo
import json
from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test
#Imports for AES API key encryption
from Crypto.Cipher import AES
import base64
# Email imports for contact view
from django.core.mail import BadHeaderError, EmailMessage, send_mail
#Notifications import for toastr pop ups
from django.contrib import messages
#Imports the links stored in variables of the API calls 
from points.APIcalls import *
#Imports the cost for each of the activities stored in an integer variable
from points.costValues import * 
# encrypt all the sensitve data
from points.encrypt import *
cipher = Cryptor()
enc_key = cipher.encrypt(APIkeys)

#View to define the back-end functionality for user registration
def register(request):
    registered = False 

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        studentID = request.POST.get('StudentID', None)
        password = request.POST.get('password', None)
        
        #Store the user password and username, sent it via the api by post request, and moodle authenticates it
        myobj = {'username':studentID,'password':password, 'encrypted_key':enc_key} 

        #This sends a request to the moodle API
        r = requests.post(loginAPIcall, data = myobj)

        valid = r.json()
    
        # The status 1 indicate this user is valid in moodle
        if user_form.is_valid() and profile_form.is_valid() and valid['status']==1:
            id=valid['userinfo']['id']
            request.session['id'] = id
            request.session['username'] = valid['userinfo']['username'] 
            user = user_form.save(commit=False)
            user.set_password(user.password)
            user.save()
            studentProfileInfo = profile_form.save(commit=False)
            studentProfileInfo.user = user
            studentProfileInfo.StudentID = studentID
            studentProfileInfo.save()
            
            #Displays notification if the user has successfully registered
            messages.success(request, "Successfully Registered!")

            login(request,user)
        else:
            if valid['status']==0:

                #Displays error message if the details the user has entered is incorrect
                messages.error(request, "The Moodle username or password is incorrect")
    else:
        #Else request type is invalid, so save the forms and display them to the user 
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request,'points/register.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})

#This view provides the back-end for the user login page
def user_login(request):
    if request.method == 'POST':

        #Gets the user details from Django
        username = request.POST.get('username')
        studentID = request.POST.get('studentID')
        password = request.POST.get('password')
        myobj = {'username': studentID,'password':password, 'encrypted_key':enc_key}

        #Send related user info to moodle (moodle side has auth passwor API function)
        r = requests.post(loginAPIcall, data = myobj)
        d=r.json()

        #Authentictes the user in dajngo
        user = authenticate(username=username, studentID = studentID, password=password)
        
        if user:
            if user.is_active:   
                # status 1 indicated this user is a user, so we login this user
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
            try:
                u = User.objects.get(username=username)
                u.set_password(password)
                u.save()
                user2 = authenticate(username=username, studentID = studentID, password=password)
                messages.success(request, "Sucessfully logged in! Welcome!")
                login(request,user2)
                return HttpResponseRedirect(reverse('index'))    
            except:
                messages.error(request, "Please enter the correct username!")         
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            messages.error(request, "Incorrect username or password!")
    return render(request, 'points/login.html', {})

#View used for Re-Wire Game Provides back-end functionaility to see if the user can afford to play the game or not
def game1(request):
    id=request.session['id']
    myobj = {'user_id': id, 'encrypted_key' : enc_key}

    #Calls the API to get the active users points
    r = requests.post(getPointsAPIcall, data = myobj)
    d=r.json()

    #If user has points more than the points required to play the game let them play
    if int(d['points']) >= gameCost:
        myobj = {'user_id': id, 'points':str(gameCost), 'encrypted_key' : enc_key}

        #Calls the API to remove user points from Moodle
        r = requests.post(removePointsAPIcall, data = myobj)

        #User can afford so display game
        return render(request,'points/game1.html')

    else:
        #Else reject the user from playing them game
        messages.error(request, "You don't have enough points to play!")
        return HttpResponseRedirect(reverse('index'))

#View used for Tic Tax Toe game
def game2(request):

    # get the session id to auth user
    id=request.session['id']
    myobj = {'user_id': id, 'encrypted_key' : enc_key}

    # call the get user points api 
    r = requests.post(getPointsAPIcall, data = myobj)
    d=r.json()

    # if user has points more than 5 then play game
    if int(d['points']) >= gameCost:
        myobj = {'user_id': id, 'points':str(gameCost), 'encrypted_key' : enc_key}
        r = requests.post(removePointsAPIcall, data = myobj)
        return render(request,'points/game2.html')
    else:
        messages.error(request, "You don't have enough points to play!")
        return HttpResponseRedirect(reverse('index'))


#View used to retrieve the users points from the Moodle server
def getmypoint(request):

    #retrieves session ID
    id=request.session['id']
    myobj = {'user_id': id, 'encrypted_key' : enc_key}

    #Retrieves the number of points the user currently has
    noOfPoints = requests.post(getPointsAPIcall, data = myobj)

    #Returns the number of points
    return HttpResponse(noOfPoints)

#Provides the back end functionality to calcualte the points the user has spent and the total points they have earned
def pointcalculate(request):
    id=request.session['id']
    myobj = {'user_id': id, 'encrypted_key' : enc_key}

    #API call to get the user points list
    r = requests.post(transactionsAPIcall, data = myobj)
    d=r.json()
    if d['status']==1:
        point_d = d['rows']
        total_point = 0
        spent_point = 0
        #Loops through points list and calculates points
        for i in range(len(point_d)):
            if (point_d[i]['type'] == '-'):
                spent_point += int(point_d[i]['amount'])
            else:
                total_point +=int(point_d[i]['amount'])
        #Updates the variable stroing the JSON information
        d.update({'total_point':total_point})
        d.update({'spent_point':spent_point})
    else:
        return JsonResponse({'total_point':0,'spent_point':0})
    #Returns the calculated variables via a JSON response
    return JsonResponse(d)

#Provides back-end fucntionality for users changing their username
def changeUsername(request):
    id=request.session['id'] 
    user = request.user 
    username = request.GET.get('username', None) 
    
    #Checks to see if the username already exists
    try:
        mightBeOtherusername = User.objects.get(username=username)
        invalid = {"status":0,'message':'  This username already exist for other user!'}
        return JsonResponse(invalid)
    except:

        #If they are trying to change it to the same username reject the action
        if request.user.username == username: 
            invalid = {"status":0,'message':'  Do not enter the same username!'}
            return JsonResponse(invalid)
        else:

            # If they are not the same then it is valid
            myobj = {'user_id': id, 'points': str(changeNicknameCost), 'action':'update','alternatename': username, 'encrypted_key' : enc_key}
             #Calls the API to update the OGRE points of the user
            r = requests.post(changeNicknameAPIcall, data = myobj)
            d = r.json()

            #If not equal to 0 update the username
            if d["status"] != 0:
                u = User.objects.get(username=request.user.username)
                u.username = username
                u.save()
            
        #Returns the request
            return HttpResponse(r)   
     

#Displays the list of points to the user if they are logged in
def pointlist(request): 
    id=request.session['id']
    myobj = {'user_id': id, 'encrypted_key' : enc_key}
    r = requests.post(transactionsAPIcall, data = myobj)
    data = r.json()
    if data['status'] == 1:
        pointlist = data["rows"]
    else:
        pointlist = [{'type': 'null', 'detail': 'null', 'amount': 'null', 'userid': 'null', 'spentTime': 'null'}]
        messages.error(request, "you do not have points transaction!")         
    return render(request,'points/pointlist.html', {"pointlist": pointlist})

# View that displays the points leaderboard to the user, using data from Moodle
def leaderboard(request):
    id = request.session['id']
    myobj = {'user_id': id, 'encrypted_key' : enc_key}

    # API call to the leader board php file in the Moodle server
    r = requests.post(leaderboardAPIcall, data = myobj)

    data = r.json()
    leaderboard = data["rows"]
    return render(request, 'points/leaderboard.html', {"leaderboard": leaderboard})

#Provides back-end fucntionality for changing your avatar
def changeAvatar(request):
    if request.method == 'POST':
        if 'image' in request.FILES:
            id=request.session['id']
            myobj = {'user_id': id, 'encrypted_key' : enc_key}
            r = requests.post(getPointsAPIcall, data = myobj)
            d=r.json()
            if d['status'] == 1:
                if int(d['points']) >= changeAvatarCost:
                    myobj = {'user_id': id, 'points' : str(changeAvatarCost), 'encrypted_key' : enc_key}
                    r = requests.post(changeAvatarAPIcall,data = myobj)
                    u = User.objects.get(username=request.user.username)
                    d = r.json()
                    u.studentprofileinfo.profile_pic = request.FILES['image']
                    u.studentprofileinfo.save()
                    messages.success(request, "Successfully update your avatar")
                    return HttpResponseRedirect(reverse('index'))    
                else:
                    messages.error(request, "you do not have enough points!")
            else:
                    messages.error(request, "you do not have enough points!")
        else:
            messages.error(request, "something went wrong!")         
    return render(request, 'points/shop.html')



#Provides the back end functionaility for the contact page
def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        #If the form is valid send the email to the account
        if form.is_valid():
            contact_name = form.cleaned_data['contact_name']
            contact_email = form.cleaned_data['contact_email']
            subject = form.cleaned_data['subject']
            content = form.cleaned_data['content']
            message = "Name: " + contact_name + "\nEmail: " + contact_email +  "\nMessage: " + content
            email = EmailMessage(subject, message,
                                to=['contactogre2020@gmail.com']) #change to your email
            email.send()
            #Redirect them to the thank you page
            return redirect('../thanks/')
    #Returns the contact page when requested
    return render(request, 'points/contact.html', {'form': form})

#Displays the list a list of games the user can play when requested
@login_required
def game_menu(request):
    context_dict = {}
    return render(request, 'points/game_menu.html', context_dict)

#View used for allowing users to navigate to login page if they AREN'T logged in
@login_required
def index(request):
    return render(request, 'points/index.html')

#View used for redirecting user to login page when they log out
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

#Displays profile page to the user when requested
def profile(request):
    return render(request, 'points/profile.html')

#Displays OGRE points page to the user when requested
def ogre_points(request):
    return render(request, 'points/ogre_points.html')

#Displays about page to the user when requested
def about(request):
    return render(request, 'points/about.html')

#Displays the thanks page to the user when they request the page
def thanks(request):
    return render(request, 'points/thanks.html')

#Displays FAQ page to the user when requested
def faq(request):
    return render(request, 'points/faq.html')

#Makes sure user is an admin to see the JSON files for testing purposes
@user_passes_test(lambda u: u.is_superuser)
def iterateJSON(request):
    return render(request, 'points/iterateJSON.html')
   
