from django import forms
class SignInForm(forms.Form):
    user_name = forms.CharField(max_length=30,
    widget = forms.TextInput(attrs={
        'class' : 'form-control', 'placeholder' : 'User Name'
    }))

    user_email = forms.CharField(max_length=30, widget = forms.EmailInput(attrs={
        'class' : 'form-control', 'placeholder' : 'Email Address'
    }))

    user_password = forms.CharField(max_length=30, widget=forms.PasswordInput(attrs={
        'class' : 'form-control', 'placeholder' : 'Password'
    }))