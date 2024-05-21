from django import forms

class Registration(forms.Form):
    username = forms.CharField(max_length=30)
    first_Name=forms.CharField(max_length=25)
    last_Name=forms.CharField(max_length=25)
    age=forms.IntegerField(max_value=100)
    email=forms.EmailField()
    