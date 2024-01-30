from django import forms
from .models import state

class stateform(forms.ModelForm):
    class Meta:
        model = state
        fields = "__all__"
    

