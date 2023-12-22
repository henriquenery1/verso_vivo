from django.views import View
from django.http import HttpResponse
from django.shortcuts import render

class ExampleView(View):
    def get(self, request):
        return HttpResponse("<h1>Hello world!</h1>")
