from django import forms
from .models import Video
class NewVideoForm(forms.Form):
    title       = forms.CharField(widget=forms.TextInput(attrs={
        "class":"form-control",
        "id":"title-input",
        "placeholder":"Title...",
        "maxlength":"40"
    }))
    thumbnail = forms.FileField(widget=forms.FileInput(attrs={
        'accept':'image/*',

    }))

    video = forms.FileField(widget=forms.FileInput(attrs={
        'accept':'video/*',

    }))

    description = forms.CharField(widget=forms.Textarea)