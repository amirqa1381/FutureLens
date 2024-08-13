from django import forms


class GetFile(forms.Form):
    file = forms.FileField(label='Select a file', widget=forms.FileInput(attrs={'class':'form-control'}))