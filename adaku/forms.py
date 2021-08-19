from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
    email = forms.EmailField(label= 'Your email', max_length=254)
    address = forms.CharField(label= 'Contact address') 
    phone = forms.CharField(label= 'Phone number')