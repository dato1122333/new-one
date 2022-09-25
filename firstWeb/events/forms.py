from django import forms
from django.forms import ModelForm
from .models import Venue


#Create a From Here


class VenueForm(ModelForm):
    class Meta:
        model = Venue
        fields = "__all__"

        labels = {
            'name': '',
            'email': '',
            'address': '',
            'owner_phone': '',
            'client_phone': '',
            'my_date': '',
            'my_time': '',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'სახელი სრულად'}),
            'email': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'ელ-ფოსტა'}),
            'address': forms.TextInput(attrs={'class':'form-control', 'placeholder':'მისამართი'}),
            'owner_phone': forms.TextInput(attrs={'class':'form-control', 'placeholder':"მეპატრონის ნომერი"}),
            'client_phone': forms.TextInput(attrs={'class':'form-control', 'placeholder':"კლიენტის ნომერი"}),
            'my_date': forms.TextInput(attrs={'class':'form-control', 'placeholder':'რიცხვი და თვე'}),
            'my_time': forms.TextInput(attrs={'class':'form-control', 'placeholder':'ზუსტი დრო მაგ: 13:50'}),
        }
        