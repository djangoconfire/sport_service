from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,get_user_model,authenticate

from user_profile.models import UserProfile

User=get_user_model()

def InvalidUsernameValidator(value):
   if '@' in value or '+' in value or '-' in value:
         raise ValidationError('Enter a valid username.')

def UniqueEmailValidator(value):
   if User.objects.filter(email__iexact=value).exists():
         raise ValidationError('User with this Email already exists.')

def UniqueUsernameIgnoreCaseValidator(value):
   if User.objects.filter(username__iexact=value).exists():
         raise ValidationError('User with this Username already exists.')

class SignUpForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),
         max_length=30,
         required=True,
         help_text='Usernames may contain <strong>alphanumeric</strong>, <strong>_</strong> and <strong>.</strong> characters')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}), 
         label="Confirm your password",
         required=True)
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control'}), 
         required=True,
         max_length=75)

    class Meta:
         model = UserProfile
         exclude = ['last_login', 'date_joined']
         fields = ['username', 'email', 'password', 'confirm_password']

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].validators.append(InvalidUsernameValidator)
        self.fields['username'].validators.append(UniqueUsernameIgnoreCaseValidator)
        self.fields['email'].validators.append(UniqueEmailValidator)

    def clean(self):
        super(SignUpForm, self).clean()
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password and password != confirm_password:
            self._errors['password'] = self.error_class(['Passwords don\'t match'])
        return self.cleaned_data


class UserLoginForm(forms.Form):
    username = forms.CharField(label="Username", max_length=30, 
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Password", max_length=30, 
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password'}))


    def clean(self,*args,**kwargs):
        username=self.cleaned_data.get("username")
        password=self.cleaned_data.get("password")
        

        if username and password:
            user=authenticate(username=username,password=password)
            if not user:
                raise forms.ValidationError("User does not Exist")

            if not user.check_password(password):
                raise forms.ValidationError("Incorrect Password")

            if not user.is_active:
                raise forms.ValidationError("account is not active") 

        return super(UserLoginForm,self).clean(*args,**kwargs)           
