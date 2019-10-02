from django import forms

class login_form(forms.Form):
    username = forms.CharField(label="Username",max_length=30)
    password = forms.CharField(label="Password",max_length=30,widget=forms.PasswordInput)

class owner_account_form(forms.Form):
    name = forms.CharField(label="Name",max_length=30)
    address = forms.CharField(label="Address",max_length=100)
    contact1 = forms.IntegerField(label="Contact1")
    contact2 = forms.IntegerField(label="Contact2")
    L = forms.IntegerField()
    M = forms.IntegerField()
    H = forms.IntegerField()
    username = forms.CharField(label="Username",max_length=30)
    password = forms.CharField(label="Password",max_length=30,widget=forms.PasswordInput)

class customer_account(forms.Form):
    name = forms.CharField(label="Name",max_length=30)
    address = forms.CharField(label="Address",max_length=100)
    contact1 = forms.IntegerField(label="Contact1")
    contact2 = forms.IntegerField(label="Contact2")


