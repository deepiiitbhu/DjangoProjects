from django.http import HttpResponse

''' def home(request):
    print(dir(request))
    print(request.content_type)
    print(request.path)
    return HttpResponse("<h1> Hello word </h1>") '''


def home(request):
    response = HttpResponse()
    response.write("<p> page not found </p>")
    response.status_code =404

    return response

