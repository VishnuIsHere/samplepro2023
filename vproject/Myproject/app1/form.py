from . models import *
from django.forms import ModelForm


class gameform(ModelForm):
    class Meta:
        model = Games
        fields = '__all__'