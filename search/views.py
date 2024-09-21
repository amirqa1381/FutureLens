from django.shortcuts import render
from django.http import HttpRequest
from django.contrib.auth.models import User
from django.db.models import Q


def search_view(request: HttpRequest):
    """
    View function for handling search queries.
    Args:
        request (HttpRequest): _description_
    """
    if  request.method == "POST":
        searched = request.POST.get('searched', None)
        results = request.user.userfiles_set.filter(Q(title__icontains=searched) | Q(slug__icontains=searched) & Q(cleaned=True))
        if results is not None:
            context = {
            'results': results
            }
        else:
            context = {"text": "Nothing found!!!!!"}
        return render(request, "search/search.html", context)
        
        