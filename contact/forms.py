from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        exclude = ('user', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['type'].widget.attrs.update({
            'class': 'form-control ',
            'name': 'typetask',
            'required': 'required',
            'placeholder': 'Select Type Task'
        })
        self.fields['file'].widget.attrs.update({
            'type': 'file',
            'class': 'form-control',
            'name': 'file',
            'placeholder': 'Upload File'
        })
        self.fields['task'].widget.attrs.update({
            'class': 'form-control',
            'name': 'task',
            'required': 'required',
            'rows': '9',
            'placeholder': 'Enter Your Request'
        })