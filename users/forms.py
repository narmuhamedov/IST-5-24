from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from users.models import CustomUser

from captcha.fields import CaptchaField


class CustomAuthForm(AuthenticationForm):
    captcha = CaptchaField(label='введите код с картики')



GENDER = (
        ('М', 'М'),
        ('Ж', 'Ж')
)

class CustomUserForm(UserCreationForm):
    photo = forms.ImageField(required=True)
    gender = forms.ChoiceField(choices=GENDER, required=True)
    phone = forms.CharField(max_length=20, required=True, initial="+996")
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = (
            'username',
            'password1',
            'password2',
            'photo',
            'first_name',
            'email',
            'phone',
            'gender'
        )
        def save(self, commit=True):
            user = super(CustomUserForm, self).save(commit=False)
            user.email = self.cleaned_data['email']
            if commit:
                user.save()
            return user