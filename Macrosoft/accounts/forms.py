from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username',
                  'first_name',
                  'last_name',
                  'email',
                  'password1',
                  'password2'
        )

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = {
            'email',
            'last_name',
            'first_name'

        }

class ApplicationSubmitForm(forms.Form):

    author = forms.CharField(max_length=30)
    app_name = forms.CharField(max_length=30)
    description = forms.CharField(max_length=500)
    weblink = forms.CharField(max_length=200)
    version = forms.CharField(max_length = 50)
    platform = forms.CharField(max_length=50)
    price = forms.FloatField()




