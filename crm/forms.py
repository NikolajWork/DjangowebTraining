from django import forms

class Orderform(forms.Form):
    name = forms.CharField(max_length=200, widget=forms.TextInput(attrs=({'class': 'form-control'})))
    phone = forms.CharField(max_length=200, widget=forms.TextInput(attrs=({'class': 'form-control'})))