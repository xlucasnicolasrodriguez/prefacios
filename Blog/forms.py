from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from Blog.models import Avatar


class FormularioPosteo(forms.Form):

    autor = forms.CharField(max_length=40)
    email = forms.EmailField()
    titulo = forms.CharField(max_length=40)
    cuerpo = forms.CharField(widget=forms.Textarea)
    imagen = forms.ImageField()


class FormularioBusqueda(forms.Form):

    titulo = forms.CharField(max_length=40)


class FormularioRegistroUsuario(UserCreationForm):

    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Confirme su contraseña", widget=forms.PasswordInput
    )

    class Meta:

        model = User
        fields = ["username", "password1", "password2"]
        help_texts = {"username": None, "password1": None, "password2": None}


class AvatarFormulario(forms.ModelForm):
    class Meta:

        model = Avatar
        fields = ["user", "imagen"]


class UserEditionForm(UserCreationForm):
    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")
    email = forms.EmailField(label="Modificar email")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "password1", "password2"]
        help_texts = {k: "" for k in fields}
