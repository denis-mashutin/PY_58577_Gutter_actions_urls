from django.urls import path, include
from .views import *


urlpatterns = [
    path("hello/func/", hello_world_view, name="hello_django"),
    path("hello/class/", HelloWorldView.as_view(), name="hello_django_class"),
    path("book/", BookDetailView.as_view(), name="book"),
    path("book/create/", BookCreateView.as_view(), name="create_book"),
    path("book/delete/", BookDeleteView.as_view(), name="delete_book"),
    path("include/", include(fff))
]
