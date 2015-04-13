from django import forms
from django.contrib.auth.models import User
from salon.models import Comments

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password','email','first_name', 'last_name')

class CommentForm(forms.ModelForm):

    text = forms.CharField(max_length=300,  widget=forms.Textarea)
    class Meta:
        model = Comments
        fields =('text',)