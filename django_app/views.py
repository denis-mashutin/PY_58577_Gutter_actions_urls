from django.views import View
from django.http import HttpResponse
from django.views.generic import CreateView, DeleteView, DetailView
from .models import Book
from django.views.decorators.http import require_POST
from rest_framework import viewsets
from .serializers import BookSerializer
from rest_framework.decorators import action
from rest_framework.response import Response



@require_POST
def hello_world_view(request):
    return HttpResponse("Hello World")


class HelloWorldView(View):
    def get(self, request):
        return HttpResponse("Hello World")

    def post(self, request):
        return HttpResponse("Hello World")


class BookCreateView(CreateView):
    model = Book
    fields = ['title', 'author', 'publication_date']


class BookDeleteView(DeleteView):
    model = Book


class BookDetailView(DetailView):
    model = Book


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    @action(detail=True, methods=['get'])
    def custom_method(self, request, pk=None):
        book = self.get_object()
        # Do something with book
        data = {"message": "This is a custom method"}
        return Response(data)
