from django.shortcuts import render
from django.http import HttpResponse

from .models import PostModel
# Create your views here.
 # CRUD : Create, Retreive, Update, Delete, List
def post_model_list_view(request):
    qs = PostModel.objects.all()
    print(qs)

    print(request.user)
    if request.user.is_authenticated():
        print("logged in")
    else:
        print("Not logged in")
    # return HttpResponse("some data")
    template_path = "blog/list-view.html"
    #context_dictionary = {}
    context_dictionary = {
        "object_list": qs
    }
    return render(request, template_path, context_dictionary)

