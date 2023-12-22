from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from .models import Content


class ContentView(View):
    template_name = "contents/content_list.html"

    def get(self, request):
        contents = Content.objects.all()
        return render(request, self.template_name, {'contents': contents})