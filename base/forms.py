from django import forms
from django.forms.widgets import DateTimeInput
from .models import Task

class PositionForm(forms.Form):
    position = forms.CharField(max_length=100)

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'dayin', 'complete']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'dayin': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),
            'complete': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields['dayin'].input_formats = ['%Y-%m-%dT%H:%M']
