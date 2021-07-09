from django import forms
from .models import *

class AddWiget(forms.ModelForm):
    class Meta:
        model = OBS_Model
        fields = "__all__"