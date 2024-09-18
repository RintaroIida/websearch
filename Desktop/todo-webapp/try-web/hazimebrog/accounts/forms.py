from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model


User = get_user_model()

class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text='メールアドレスを入力')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class EmailLoginForm(AuthenticationForm):
    username = forms.EmailField(label="Email")

