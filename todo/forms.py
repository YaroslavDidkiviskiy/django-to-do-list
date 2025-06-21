from django import forms
from todo.models import Task, Tag


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        # Remove 'datetime' from the fields list
        fields = ["content", "deadline", "is_done", "tags"]  # Fixed
        widgets = {
            "deadline": forms.DateTimeInput(attrs={"type": "datetime-local", "class": "form-control"}),
            "is_done": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            if isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs["class"] = "form-check-input"
            else:
                field.widget.attrs["class"] = "form-control"


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ["name",]


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            if isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs["class"] = "form-check-input"
            else:
                field.widget.attrs["class"] = "form-control"
