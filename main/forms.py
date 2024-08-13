from django import forms
from .validators import check_the_csv


class GetFile(forms.Form):
    file = forms.FileField(
        label="Select a file",
        widget=forms.FileInput(attrs={"class": "form-control"}),
        validators=[check_the_csv,],
    )
