from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Profile


class SignupForm(UserCreationForm):

    ID = forms.CharField()
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields+('email',)

    def save(self):
        user = super().save()

        profile = Profile.object.create(

            user = user,
            ID = self.cleaned_data['ID'],)
        return user

class LoginForm(AuthenticationForm):
    answer = forms.IntegerField(label='3+3=?')
    def clean_answer(self):
        if self.cleaned_data.get('answer', None) != 6:
            raise forms.ValidationError('땡~!!!')