from django import forms

class MyForm(forms.Form):
    name = forms.CharField(label='Name')
    email = forms.EmailField(label='email')
    course = forms.CharField(label='course')
