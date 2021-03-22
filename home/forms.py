from django import forms
from home.models import Feedback

class feedbackform(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = "__all__"