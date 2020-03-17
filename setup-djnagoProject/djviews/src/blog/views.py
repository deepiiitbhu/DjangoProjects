
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import PostModel
# Create your views here.
 # CRUD : Create, Retreive, Update, Delete, List

def post_model_detail_view(request, id=None):
    #obj = PostModel.objects.get(id=1)
    print("****************")
    print(id)
     print("****************")
    obj = get_object_or_404(PostModel, id=id)
    context = {
        "object": obj,
    }
    template = "blog/detail-view.html"
    return render(request, template, context)


def post_model_list_view(request):

    ''' qs = PostModel.objects.all()
    #print(qs)

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
 '''
    qs = PostModel.objects.all()
    context = {
        "object_list": qs,
    }

    template = "blog/list-view.html"
    return render(request, template, context)



