from django import forms
from points.models import StudentProfileInfo
from django.contrib.auth.models import User
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    studentID = forms.CharField()
    class Meta():
        model = User
        fields = ('username','studentID','password','email')
class UserProfileInfoForm(forms.ModelForm):
     class Meta():
         model = StudentProfileInfo
         fields = ('profile_pic',)