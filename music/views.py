from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>This will be a list of all albums</h1>")


def detail(request, album_id):
    return HttpResponse("<h2>Details for Album id: " + str(album_id) + "</h2>")
