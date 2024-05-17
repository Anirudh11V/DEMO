from .models import UserReg
from django.forms import ModelForm

from django.contrib.auth.forms import UserCreationForm


class Regform(UserCreationForm):
    class Meta:
        model=UserReg
        fields = ['name','username','email','password1','password2']

class UserForm(ModelForm):
    class Meta:
        model = UserReg
        fields = ['avatar','username','name','email','phone','bio']