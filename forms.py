from django import forms

class LoginForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
    user = forms.CharField(label='User',max_length = 100)
    password = forms.CharField(label='Password')

class SettingsForm_gen(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=254,)
    pp = forms.ImageField(required=False)
