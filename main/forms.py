
from django import forms
import csv



class UploadedFile(forms.Form):
    file = forms.FileField(
        label="Select a file",
        widget=forms.FileInput(attrs={"class": "form-control"}),
    )
    
    def clean(self):
        file = self.cleaned_data['file']
        if not file.name.endswith(".csv"):
            raise forms.ValidationError("this file is not csv file")
        if file.content_type != "text/csv":
            raise forms.ValidationError("only csv files are allowed for inserting")
        try:
            # here i want to read the file and and seek to the start of the file for with seek 
            # and with csv.reader i try to read the file 
            file.seek(0)
            csv.reader(file.read().decode("utf-8").splitlines())
        except Exception:
            raise forms.ValidationError("Invalid Csv file content")
        return file
