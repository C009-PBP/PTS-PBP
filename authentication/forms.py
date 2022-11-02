## OK
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

# from .models import Pasien, Dokter, User
from .models import User

class PasienSignUpForm(UserCreationForm):
    # interests = forms.ModelMultipleChoiceField(
    #     queryset=Subject.objects.all(),
    #     widget=forms.CheckboxSelectMultiple,
    #     required=True
    # )


    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(PasienSignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control register-pasien'
        self.fields['password1'].widget.attrs['class'] = 'form-control register-pasien'
        self.fields['password2'].widget.attrs['class'] = 'form-control register-pasien'

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_pasien = True
        user.save()
        # pasien = Pasien.objects.create(user=user)
        # print("TES CREATE PASIEN")
        return user


class DokterSignUpForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(DokterSignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control register-dokter'
        self.fields['password1'].widget.attrs['class'] = 'form-control register-dokter'
        self.fields['password2'].widget.attrs['class'] = 'form-control register-dokter'

        for fieldname in ['username', 'password1', 'password2']:    
            self.fields[fieldname].help_text = None


    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_dokter = True
        if commit:
            user.save()
        return user




