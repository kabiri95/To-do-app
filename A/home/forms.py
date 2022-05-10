from django import forms


class TodoCreateForm(forms.Form):
    title = forms.CharField()
    body = forms.CharField()
    created = forms.DateTimeField()
    deadline = forms.DateTimeField(required=False)
