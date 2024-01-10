from django import forms
from .models import Consultant

class ConsultantForm(forms.ModelForm):
    class Meta:
        model = Consultant
        fields = '__all__'  # Include all fields from the model
