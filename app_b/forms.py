from django import forms

from app_b.models import Model_B


class FormModel_B(forms.ModelForm):
    
    class Meta:
        model = Model_B