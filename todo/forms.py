from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"

    deadline = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}),
                               required=False)