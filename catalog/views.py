from django.shortcuts import render
from django.http import HttpResponse
from catalog.models import Author, Book, BookInstance, Genre, Language, \
                                Publisher, Status
from django.views.generic import ListView, DeleteView, DetailView


class AuthorDetailView(DetailView):
    model = Author
    template_name = "author_detail.html"



class AuthorListView(ListView):
    model = Author
    paginate_by = 4
    template_name = "authors_list.html"



class BookDetailView(DetailView):
    model = Book 
    context_object_name = 'book'
    template_name = "book_detail.html"


class BookListView(ListView):
    model = Book
    context_object_name = 'books'
    template_name = 'book_list.html'
    paginate_by = 3 



def index(request):
    text_head = "Title Bookmarks, ..."
    books = Book.objects.all()
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    num_instances_available = BookInstance.objects.filter(status__exact=2).count()
    authors = Author.objects
    num_authors = Author.objects.count()

    context = {
        "text_head" : text_head, 
        "books" : books,
        "num_books" : num_books,
        "num_instances" : num_instances,
        "num_instances_available" : num_instances_available,
        "authors" : authors,
        "num_authors" : num_authors
    }

    return render(request, 'index.html', context)
