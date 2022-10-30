from django import forms
from .models import BMI

class Form_BMI(forms.ModelForm):
    class Meta:
        model = BMI
        fields = [
            'umur',
            'berat',
            'tinggi',
        ]

        widgets = {
            'umur' : forms.TextInput(
                            attrs={
                                'type': 'number',
                                'id' : 'umur',
                                'name' : 'umur',
                                'class' : 'form-control text-center', 
                                'style' : 'padding: 5px; border-radius: 8px', 
                                'min': "1", 
                                'required' : 'true', 
                                }),
             'berat' : forms.TextInput(
                            attrs={
                                'type': 'number',
                                'id' : 'berat',
                                'name' : 'berat',
                                'class' : 'form-control text-center', 
                                'style' : 'padding: 5px; border-radius: 8px', 
                                'min': "1", 
                                'required' : 'true',

                                }),
             'tinggi' : forms.TextInput(
                            attrs={
                                'type': 'number',
                                'id' : 'tinggi',
                                'name' : 'tinggi',
                                'class' : 'form-control text-center', 
                                'style' : 'padding: 5px; border-radius: 8px', 
                                'min': '1', 
                                'required' : 'true',
                                }),
             
        }   