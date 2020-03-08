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
# Email imports for contact view
from django.core.mail import BadHeaderError, EmailMessage, send_mail
#Notifications import for toastr pop ups
from django.contrib import messages
#Imports the links stored in variables of the API calls 
from points.APIcalls import *
#Imports the cost for each of the activities stored in an integer variable
from points.costValues import * 

#View to define the back-end functionality for user registration
def register(request):
    #Initalising registered variable
    registered = False 
    #Use post request to get Moodle related information
    if request.method == 'POST':
        #We use crispy forms, which has post request
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        studentID = request.POST.get('StudentID', None)
        password = request.POST.get('password', None)
        
        #store the user password and uername, sent it via the api by post request, moodle have the auth function for it
        myobj = {'username':studentID,'password':password} 

        #This sends a reuest to the moodle API
        r = requests.post(loginAPIcall, data = myobj)

        #if valid['status] == 1, the user is a moodle user, meaning the moodle details provided are correct
        valid = r.json()
        
        # The status 1 indicate this user is valid in moodle
        if user_form.is_valid() and profile_form.is_valid() and valid['status']==1:

            #All code to next comment is saving the users details in the Django database
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
            #Logins in the user straight away
            login(request,user)
        else:
            if valid['status']==0:
                #Displays error message if the details the user has entered is incorrext
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
    #Use post request to get related user info
    if request.method == 'POST':
        #Gets the user details from Django
        username = request.POST.get('username')
        studentID = request.POST.get('studentID')
        password = request.POST.get('password')
        #Stores username and password in an object
        myobj = {'username': studentID,'password':password}
        #Send related user info to moodle (moodle side has auth passwor API function)
        r = requests.post(loginAPIcall, data = myobj)
        d=r.json()
        #Authentictes the user in dajngo
        user = authenticate(username=username, studentID = studentID, password=password)
        print(username,studentID,password) 
        if user:
            if user.is_active:   
                # status 1 indicated this user is a user, so we login this user
                if d['status']==1:
                    id=d['userinfo']['id']
                    print(id)
                    request.session['id'] = id
                    request.session['username'] = d['userinfo']['username'] 
                    messages.success(request, "Sucessfully logged in! Welcome!")
                    login(request,user)
                    return HttpResponseRedirect(reverse('index'))

                elif d['status']==0:
                    #else the user is not a user stored so we send error message
                    messages.error(request, "Please use your moodle password!")
            else:
                messages.error(request, "Please register with your moodle account first!")

        # Used to account for if the user reset their password via moodle and then registered again
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



def game1(request):
    

    #Provides back-end functionaility to see if the user can afford to play the game or not
    myobj = {'user_id': '1',"points":5}
    # get the session id to auth user
    id=request.session['id']
    #Calls the API to get the active users points
    r = requests.get(getPointsAPIcall+id)
    d=r.json()

    #If user has points more than the points required to play the game let them play
    if int(d['points']) >= gameCost:
        #Calls the API to remove user points from Moodle
        #Variable gameCost is refrenced from costValues.py where the cost to play the game is defined
        r = requests.get(removePointsAPIcall+id+'&points='+str(gameCost))
        return render(request,'points/game.html')

    else:
        #Else reject the user from playing them game
        messages.error(request, "You don't have enough points to play!")
        return HttpResponseRedirect(reverse('index'))


def game2(request):
    myobj = {'user_id': '1',"points":5}
    # get the session id to auth user
    id=request.session['id']
    # call the get user points api 
    r = requests.get('http://157.245.126.159/api/get_user_points.php?user_id='+id, data = myobj)
    d=r.json()
    # if user has points more than 5 then play game
    if int(d['points']) >= 5:
        r = requests.get('http://157.245.126.159/api/cut_user_points.php?user_id='+id+'&points=5', data = myobj)
        return render(request,'points/game2.html')
    else:
        messages.error(request, "You don't have enough points to play!")
        return HttpResponseRedirect(reverse('index'))


#View used to retrieve the users points from the Moodle server

def getmypoint(request):
    #retrieves session ID
    id=request.session['id']
    #Retrieves the number of points the user currently has
    noOfPoints = requests.get(getPointsAPIcall+id)
    #Returns the number of points
    return HttpResponse(noOfPoints)

#Provides the back end functionality to calcualte the points the user has spent and the total points they have earned
def pointcalculate(request):
    #Gets session id
    id=request.session['id']
    #API call to get the user points list
    r = requests.get(transactionsAPIcall+id)
    #Intialisies variable stroing the JSON information
    d = r.json()
    #Stores points list in this variables for the user logged in
    point_d = d['rows']
    #Initialises the variables being calculatedß
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
    #Returns the calculated variables via a JSON response
    return JsonResponse(d)

#Provides back-end fucntionality for users changing their username
def changeUsername(request):
    id=request.session['id'] # Gets the session id
    user = request.user # Getsthe current auth user
    username = request.GET.get('username', None) #Gets the new username user entered
    try:
        
        mightBeOtherusername = User.objects.get(username=username)
        invalid = {"status":0,'message':'  This username already exist for other user!'}
        return JsonResponse(invalid)
    except:
        #If they are trying to change it to the same username reject the action
        if request.user.username == username: 
            #0 means invalid
            invalid = {"status":0,'message':'  Do not enter the same username!    '}
            return JsonResponse(invalid)
        

            
      
        else:
            # If they are not the same then it is valid
            # Calls the API to update the OGRE points of the user
            #Variable changeNicknameCost is refrenced from costValues.py where you can change the values
            r = requests.get(changeNicknameAPIcall+id+'&points='+str(changeNicknameCost)+'&action=update&alternatename='+username)

            d = r.json()
            if d["status"] != 0:
                #We now get the user by the username
                u = User.objects.get(username=request.user.username)
                #Change the username on Django
                u.username = username
                #Save the username on Django
                u.save()
        #Returns the request
            return HttpResponse(r)   
     

#Displays the list of points to the user if they are logged in
def ajaxpointlist(request): 
    id=request.session['id']
    request = requests.get(transactionsAPIcall+id)
    return HttpResponse(request)

#Displays the list of points to the user if they are logged in
def pointlist(request):
    if request.session.get('id'):
        return render(request,'points/pointlist.html')

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

#Used to display other users profiles when requested
@login_required
def get_user_profile(request, username):
    user = User.objects.get(username=username)
    return render(request, 'points/profile.html', {"user":user})

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

# View that displays the points leaderboard to the user, using data from Moodle
def leaderboard(request):
    id = request.session['id']

    # API call to the leader board php file in the Moodle server
    r = requests.get(leaderboardAPIcall + id)
    data = r.json()
    leaderboard = data["rows"]

    return render(request, 'points/leaderboard.html', {"leaderboard": leaderboard})


def changeAvatar(request):
    
    if request.method == 'POST':
       
        if 'image' in request.FILES:
            print('found the picture!')
            id=request.session['id']
            r = requests.get('http://157.245.126.159/api/get_user_points.php?user_id='+id)
            d=r.json()
            if int(d['points']) >= 5:
                r = requests.get('http://157.245.126.159/api/changeavatar.php?user_id='+id+'&points=5')
     
                u = User.objects.get(username=request.user.username)
            
                print(u.studentprofileinfo.profile_pic)
                print(request.FILES)
                u.studentprofileinfo.profile_pic = request.FILES['image']
                u.studentprofileinfo.save()
                messages.success(request, "Successfully update your avatar")
                return HttpResponseRedirect(reverse('index'))    

            else:
                messages.error(request, "you do not have enough points!")         

                        

            
            
        else:
            messages.error(request, "something went wrong!")         

   
    return render(request, 'points/shop.html')

#Makes sure user is an admin to see the JSON files for testing purposes
@user_passes_test(lambda u: u.is_superuser)
def iterateJSON(request):
    return render(request, 'points/iterateJSON.html')
   
