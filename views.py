from django.http import HttpResponse
def movie_name(request):
    return HttpResponse("this page displays informattion about the movies")
