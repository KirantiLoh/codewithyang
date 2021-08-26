from django import forms

class AddProjectForm(forms.Form):
    name = forms.CharField(max_length=100)
    desc = forms.CharField(widget=forms.Textarea)
    image = forms.ImageField()
    link = forms.URLField()
