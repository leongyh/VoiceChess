from django import forms

class CreateGameForm(forms.Form):
	creator = forms.CharField(max_length=50)
	name = forms.CharField(max_length=50)