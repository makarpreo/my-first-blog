from .models import Task
from .models import Table
from django.forms import ModelForm, TextInput, Textarea


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "task"]
        widgets = {"title": TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите название'
        }),
        "task": Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Введите описание'
        })
        }


class TableForm(ModelForm):
    class Meta:
        model = Table
        fields = ["table", "time", "table1", "table2", "table3", "table4", "table5", "table6", "table7", "table8", "table9", "table10", "table11", "table12"]
        widgets = {"table": TextInput(attrs={
            'placeholder': 'Введите название'
        }),
        "table1": TextInput(attrs={
                'placeholder': 'Введите название'
        }),
            "table2": TextInput(attrs={
                'placeholder': 'Введите название'
            }),
            "table3": TextInput(attrs={
                'placeholder': 'Введите название'
            }),
            "table4": TextInput(attrs={
                'placeholder': 'Введите название'
            }),
            "table5": TextInput(attrs={
                'placeholder': 'Введите название'
            }),
            "table6": TextInput(attrs={
                'placeholder': 'Введите название'
            }),
        "time": Textarea(attrs={
            'placeholder': 'Введите время'
        })
        }