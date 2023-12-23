from django.shortcuts import get_object_or_404, render
from django.views import View
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .forms import ContentForm
from .models import Content


class ContentView(View):
    template_name = "contents/content_list.html"

    def get(self, request):
        contents = Content.objects.all()
        return render(request, self.template_name, {'contents': contents})

class TitlesContentView(View):
    template_name = "contents/titles_content.html"

    def get(self, request):
        contents = Content.objects.all()
        return render(request, self.template_name, {'contents': contents})

    
class DetailContentView(View):
    template_name = 'contents/detail_content.html'

    def get(self, request, content_id):
        content = get_object_or_404(Content, id=content_id)
        return render(request, self.template_name, {'content': content})

class CreateContentView(CreateView):
    template_name = 'contents/create_content.html'
    model = Content
    form_class = ContentForm
    success_url = reverse_lazy('list_contents')

    def form_valid(self, form):
        return super().form_valid(form)