from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, PasswordChangeForm, SetPasswordForm, PasswordResetForm
from django.contrib.auth.models import User
from .models import *

class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        exclude = ['seller','status', 'current_price']

class LoginForm(AuthenticationForm):
    username = UsernameField(widget = forms.TextInput(attrs={'autofocus':'True', 'class':'form-control'}))
    password = forms.CharField(widget = forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))


class CustomerRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'autofocus':'True','class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    password1 = forms.CharField( label = 'Password', widget=forms.PasswordInput(attrs={ 'class':'form-control'}))
    password1 = forms.CharField( label = 'Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        
class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField( label = 'Old Password', widget=forms.PasswordInput(attrs={ 'class':'form-control'}))
    new_password1 = forms.CharField( label = 'New Password', widget=forms.PasswordInput(attrs={ 'autocomplete':'current-password', 'class':'form-control'}))
    new_password2 = forms.CharField( label = 'Confirm Password', widget=forms.PasswordInput(attrs={ 'autocomplete':'current-password', 'class':'form-control'}))

    
class MyPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    
class MySetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField( label = 'New Password', widget=forms.PasswordInput(attrs={ 'autocomplete':'current-password', 'class':'form-control'}))
    new_password2 = forms.CharField( label = 'Confirm New Password', widget=forms.PasswordInput(attrs={ 'autocomplete':'current-password', 'class':'form-control'}))
    

class CustomerProfileForm(forms.ModelForm):
    class Meta :
        model = Customer
        fields = ['name','locality','city','mobile','state','pincode',]
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'locality':forms.TextInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'mobile':forms.NumberInput(attrs={'class':'form-control'}),
            'state':forms.Select(attrs={'class':'form-control'}),
            'pincode':forms.NumberInput(attrs={'class':'form-control'})
        }
        
class AuctionForm(forms.ModelForm):
    class Meta:
        model = auction
        fields = ['item', 'seller','product','description','start_price','end_date','is_featured']

class BidForm(forms.Form):
    bid_amount = forms.DecimalField(label='Bid Amount', max_digits=10, decimal_places=2, min_value=0, required=True)

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name','email','last_login','date_joined']
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
            # Disable fields
        self.fields['email'].disabled = True
        self.fields['last_login'].disabled = True
        self.fields['date_joined'].disabled = True