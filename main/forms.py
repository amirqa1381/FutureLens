from django import forms
import csv
from .models import UserFiles




class UploadedFile(forms.ModelForm):
    """
    this is the class that we have and it's for the files that user upload
    Args:
        forms (_type_): _description_
    """
    class Meta:
        model = UserFiles
        fields = ['title', 'file']
        widgets = {
            'title': forms.TextInput(attrs={'class':"form-control"}),
            'file': forms.FileInput(attrs={'class': "form-control"}),
        }
        
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
                reader = csv.reader(file)
            except Exception as e:
                raise forms.ValidationError("Invalid Csv file content: "+ str(e))
            file.seek(0)
            return self.cleaned_data



