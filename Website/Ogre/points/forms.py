from django import forms
from points.models import StudentProfileInfo
from django.contrib.auth.models import User
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(),help_text='Required.  the password must same with your moodle ID')
    
    class Meta():
        model = User
        fields = ('username','password','email')
class UserProfileInfoForm(forms.ModelForm):
     class Meta():
         model = StudentProfileInfo
         fields = ('StudentID','profile_pic')

class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True, label="Name")
    contact_email = forms.EmailField(required=True, label="Email")
    subject = forms.CharField(required=True, label='subject')
    content = forms.CharField(
        required=True,
        widget=forms.Textarea,
        label="Message"
    )