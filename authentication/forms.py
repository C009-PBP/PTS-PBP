## OK

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

# from .models import Pasien, Dokter, User
from .models import  User

class PasienSignUpForm(UserCreationForm):
    # interests = forms.ModelMultipleChoiceField(
    #     queryset=Subject.objects.all(),
    #     widget=forms.CheckboxSelectMultiple,
    #     required=True
    # )

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_pasien = True
        user.save()
        # pasien = Pasien.objects.create(user=user)
        # pasien.interests.add(*self.cleaned_data.get('interests'))
        print("TES CREATE PASIEN")
        return user


class DokterSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_dokter = True
        if commit:
            user.save()
        return user

