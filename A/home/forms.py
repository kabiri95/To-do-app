from django import forms
from .models import Todo


class TodoCreateForm(forms.Form):
    title = forms.CharField()
    body = forms.CharField()
    created = forms.DateTimeField()
    deadline = forms.DateTimeField(required=False)

class TodoUpdateForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = '__all__'

