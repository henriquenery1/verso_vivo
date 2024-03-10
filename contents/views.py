from django.http import HttpResponseServerError
from django.shortcuts import get_object_or_404, render
from django.views import View
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

import requests
from bs4 import BeautifulSoup

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
    success_url = reverse_lazy('titles_content')

    def form_valid(self, form):
        return super().form_valid(form)
    
class SearchVerseView(View):
    template_name = "verse/verse.html"

    def get(self, request):
        try:
            response = requests.get('https://bkjfiel.com.br/versiculo-do-dia/')
            response.raise_for_status()

            html_content = response.text

            soup = BeautifulSoup(html_content, "html.parser")

            elements = soup.find_all("div", class_="flex flex-col items-center px-[4.1666vw]")

            verse_day = []
            for element in elements:
                verse_text = element.find("span", class_="font-sans").text.strip()
                verse_reference = element.find("span", class_="block").text.strip()
                verse_day.append({"text": verse_text, "reference": verse_reference})

            return render(request, self.template_name, {"verses": verse_day})
        except requests.RequestException as e:
            return HttpResponseServerError(f"Erro ao fazer a requisição: {e}")
