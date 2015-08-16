from django.forms.models import ModelForm

from backend.core.project.models import TraductionProject


class RegisterForm(ModelForm):
    
    class Meta:
        model = TraductionProject
        fields = ['first_name', 'last_name', 'email']