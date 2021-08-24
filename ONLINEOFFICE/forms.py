from django.forms import ModelForm
from .models import registration, requesttable
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [ 'first_name', 'last_name','username','email','password1', 'password2',]

class requestform(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(requestform, self).__init__(*args, **kwargs)

		self.fields['Name'].widget.attrs.update(
			{'placeholder': 'Insert Name',})

		self.fields['Date'].widget.attrs.update(
			{'placeholder': 'YYYY-MM-DD',})

		self.fields['Details'].widget.attrs.update(
			{'placeholder': 'Further Details',})
			
		self.fields['Time'].widget.attrs.update(
			{'placeholder': '8:00am-3:00pm',})
		
	class Meta:
		model = requesttable
		fields = ['Name','Purpose','Details','Date','Time']

class StatusForm(ModelForm):
	class Meta:
		model = requesttable
		fields = ['Status']