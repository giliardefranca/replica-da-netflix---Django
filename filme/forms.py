from django.contrib.auth.forms import UserCreationForm
from .models import Usuario
from django import forms

class Formhomepage(forms.Form):
    email = forms.EmailField(label=False)


class Criarusuario(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = Usuario
        fields = ("username", "email", "password1", "password2")
