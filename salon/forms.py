from django import forms
from django.contrib.auth.models import User
from salon.models import Comments, Reservation
from bootstrap3_datepicker import DatePickerInput

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

class ReservationForm(forms.ModelForm):

    date = forms.DateField(widget=DatePickerInput())
    #date = forms.DateField()
    time = forms.TimeField()

    class Meta:
        model = Reservation
        fields =('date','time')