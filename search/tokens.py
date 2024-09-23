import uuid
from django.core.cache import cache

TOKEN_EXPIRATION_TIME = 60 * 60

def generate_token(query):
    """
    here we get the query and generate a token for it
    Args:
        query (_type_): queryset that we have
    """
    token = uuid.uuid4().hex
    cache.set(token, query, TOKEN_EXPIRATION_TIME)
    return token


def retrive_query_from_token(token):
    """
    we find the query based on the token that we pass to the function
    Args:
        token (_type_): token that we have
    """
    query = cache.get(token)
    if query:
        # remove the token from the cach after use
        cache.delete(token) 
    return query