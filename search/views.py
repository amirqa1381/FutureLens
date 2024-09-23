from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.db.models import Q
from .tokens import generate_token, retrive_query_from_token


def search_view(request: HttpRequest):
    """
    View function for handling search queries.
    Args:
        request (HttpRequest): _description_
    """
    if request.method == "POST":
        query = request.POST.get("searched", None)
        token = generate_token(query)
        return redirect("", args=[token])
    

def search_result(request: HttpRequest, token):
    """
    this funciton is for the finding the result base of the token that is provided
    Args:
        request (HttpRequest): _description_
        token (_type_): _description_
    """
    query = retrive_query_from_token(token=token)
    results = request.user.userfiles_set.filter(Q(title__icontains=query) | Q(slug__icontains=query) & Q(cleaned=True))
    context = {
        "results": results
    }
    return render(request, "search/search.html", context)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        