from django import forms

class SearchForm(forms.Form):
    """
    this class is for the search form and here every user can write all the things that want 
    and we proceed it for the user and we find and retrive the result fot the user
    Args:
        forms (_type_): _description_
    """
    query = forms.CharField(max_length=150, verbose_name="Query")
    