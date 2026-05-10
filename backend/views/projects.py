from django.http import JsonResponse, HttpRequest
from django.conf import settings
from github import Github
from github import Auth
import functools
from typing import Callable
from backend.serializers import ProjectSerializer
from rest_framework.renderers import JSONRenderer

def authenticate(view : Callable) -> Callable:
    @functools.wraps(view)
    def wrapper(*args, **kwargs):
        auth = Auth.Token(settings.GITHUB_AUTH_KEY)
        g = Github(auth=auth)
        result = view(g, *args, **kwargs)
        g.close()
        return result
    return wrapper
    
@authenticate
def get_projects(g, request : HttpRequest) -> JsonResponse:
    repos = g.get_user().get_repos()

    #convert the PaginatedList of repos to a list
    repo_list = [repo for repo in repos]
    serializer = ProjectSerializer(repo_list, many=True)
    return JsonResponse(serializer.data, safe=False)
