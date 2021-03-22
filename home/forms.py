from django import forms
from home.models import Feedback
from home.models import Contactus

class feedbackform(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = "__all__"

class contactform(forms.ModelForm):
    class Meta:
        model = Contactus
        fields = "__all__"