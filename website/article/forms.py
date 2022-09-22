from django.forms import ModelForm
from django import forms
from .models import Article
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class FormArticle(ModelForm):
    class Meta:
        model = Article
        fields = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L')
        labels = {
                'A':'A1',
                'B':'Number', 
                'C':'1st', 
                'D':'2, 3', 
                'E':'4, 5', 
                'F':'6', 
                'G':'7', 
                'H':'8', 
                'I':'9', 
                'J':'10, 11', 
                'K':'12',
                'L':'13, 14',
                }

        widgets = {
                'A':forms.Select(attrs={'class':'form-select'}),
                'B':forms.Select(attrs={'class':'form-select'}), 
                'C':forms.Select(attrs={'class':'form-select'}), 
                'D':forms.Select(attrs={'class':'form-select'}), 
                'E':forms.Select(attrs={'class':'form-select'}), 
                'F':forms.Select(attrs={'class':'form-select'}), 
                'G':forms.Select(attrs={'class':'form-select'}), 
                'H':forms.Select(attrs={'class':'form-select'}), 
                'I':forms.Select(attrs={'class':'form-select'}), 
                'J':forms.Select(attrs={'class':'form-select'}), 
                'K':forms.Select(attrs={'class':'form-select'}),
                'L':forms.Select(attrs={'class':'form-select'}),
                }

class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    address = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2', 'address')
    
    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'