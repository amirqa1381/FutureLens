from django import forms
import csv
from .models import UserFiles
import logging
import mimetypes



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
        """
        this function is for checking the csv file 
        """
        logger = logging.getLogger(__name__)
        file = self.cleaned_data["file"]
        
        # here we get the type of the file that we have and after that we can check it
        file_type, _ = mimetypes.guess_type(file.name)
        if file_type not in ['text/csv', 'application/vnd.ms-excel', 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet']:
            logger.error("invalid type %s: ", file_type)
            raise forms.ValidationError("only Csv files are allowed for inserting")
        return self.cleaned_data
        
        


