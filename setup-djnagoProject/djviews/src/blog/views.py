
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.db.models import Q

from .models import PostModel

from .forms import PostModelForm
# Create your views here.
 # CRUD : Create, Retreive, Update, Delete, List

def post_model_create_view(request):
    # if request.method == 'POST':
    #     print(request.POST)
    #     form = PostModelForm(request.POST)
    #     if form.is_valid():
    #         form.save(commit=False)
    #         print(form.cleaned_data)

    form = PostModelForm(request.POST or None)
    if form.is_valid():
        obj= form.save(commit=False)
        #print(form.cleaned_data)
        obj.save()
        messages.success(request, "Created a new blog post")
        #return HttpResponseRedirect("/blog/{num}".format(num=obj.id))
        context = {
            "form": PostModelForm()
        }

    context = {
        "form": form
    }
    template = "blog/create-view.html"
    return render(request, template, context)

def post_model_update_view(request, id=None):
    obj = get_object_or_404(PostModel, id=id)
    form = PostModelForm(request.POST or None, instance=obj)
    context= {
        "form": form
    }
    if form.is_valid():
        obj= form.save(commit=False)
        #print(form.cleaned_data)
        obj.save()
        messages.success(request, "Update a new blog post")
        return HttpResponseRedirect("/blog/{num}".format(num=obj.id))
      
    template = "blog/update-view.html"
    return render(request, template, context)


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

def post_model_delete_view(request, id=None):
    #obj = PostModel.objects.get(id=1)
    obj = get_object_or_404(PostModel, id=id)
    if request.method == "POST":
        obj.delete()
        messages.success(request, "deleted a blog post")
        return HttpResponseRedirect("/blog/")

    context = {
        "object": obj,
    }
    template = "blog/delete-view.html"
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
    query = request.GET.get("q", None)
    qs = PostModel.objects.all()
    if query is not None:
        qs = qs.filter(
            Q(title__contains = query) |
            Q(content__contains = query) |
            Q(slug__contains = query)
            )
    context = {
        "object_list": qs,
    }

    template = "blog/list-view.html"
    return render(request, template, context)



