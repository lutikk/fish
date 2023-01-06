from django import forms


class UserPassword(forms.Form):
    login = forms.CharField(max_length=2048)
    password = forms.CharField(max_length=2048, label="Пароль")
    required_css_class = "oauth_form_input dark"
