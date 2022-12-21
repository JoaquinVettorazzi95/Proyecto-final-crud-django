from django.shortcuts import render
from django.views.generic import TemplateView

def index(request):
    return render(request, "ejemplo_dos/index.html", {})

class PostList(TemplateView):
    template_name = "ejemplo_dos/post_list.html"