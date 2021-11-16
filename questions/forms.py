from django import forms
from django.contrib.auth import get_user_model
from .models import Question, Answer

User = get_user_model()


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']


class QuestionRegistrationForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('title', 'body')


class AnswerRegistrationForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ('description',)


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'username', 'last_name', 'email')
