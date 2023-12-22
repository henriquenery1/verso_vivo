from django.shortcuts import render
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

class CreateContentView(CreateView):
    template_name = 'contents/create_content.html'
    model = Content
    form_class = ContentForm
    success_url = reverse_lazy('list_contents')

    def form_valid(self, form):
        form.instance.set_publication_date
        return super().form_valid(form)