from django.shortcuts import render

# Create your views here.
from django.views import View

class IndexView(View):
    def get(self, request):
        return render(request, 'test_graph/index.html', {})

class DataUpView(View):
    def get(self, request):
        return render(request, 'test_graph/data_up.html', {})

class GraphView(View):
    def get(self, request):
        return render(request, 'test_graph/graph.html', {})