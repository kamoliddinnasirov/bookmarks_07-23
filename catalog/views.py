from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from catalog.models import Author, Book, BookInstance, Genre, Language, \
                                Publisher, Status
from django.views.generic import ListView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from catalog.forms import Form_add_author, Form_edit_author
from django.urls import reverse






def delete(request, id):
    try:
        author = Author.objects.get(id=id)
        author.delete()
        return HttpResponseRedirect("/edit_authors/")
    except:
        return HttpResponseNotFound("<h2>Author not found</h2>")

def add_author(request):
    form = Form_add_author(request.POST, request.FILES)
    if form.is_valid():
        first_name = form.cleaned_data.get("first_name")
        last_name = form.cleaned_data.get("last_name")
        date_of_birth = form.cleaned_data.get("date_of_birth")
        about = form.cleaned_data.get("about")
        photo = form.cleaned_data.get("photo")

        obj = Author.objects.create(
            first_name=first_name,
            last_name=last_name,
            date_of_birth=date_of_birth,
            about=about,
            photo=photo
        )

        obj.save()

        return HttpResponseRedirect(reverse("authors-list"))
    else:
        form = Form_add_author()
        context = {"form" : form}
        return render(request, "authors_add.html", context)



def edit_author(request, id):
    author = Author.objects.get(id=id)
    if request.method == 'POST':
        instance = Author.objects.get(pk=id)
        form = Form_edit_author(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/edit_authors/")
    else:
        form = Form_edit_author(instance=instance)
        content ={"form" : form}
        return render(request, "edit_author.html", content)

    # context = {"author": author}
    # return render(request, "edit_authors.html", context)

class LoanedBooksByUserListView(LoginRequiredMixin, ListView):
    model = BookInstance
    template_name = 'bookinstance_list_customer_user.html'
    paginate_by = 10
    def get_queryset(self):
        return BookInstance.objects.filter(
            customer=self.request.user).filter(
                status__exact='2').order_by("due_back")



def about(request):
    text_head = "About us"
    name = "OOO Kamoliddin online book shop"
    rab1 = "System developments"
    rab2 = "Book write"
    rab3 = "Book read"
    rab4 = "Create online book for peoples"

    context = {
        "text_head" : text_head,
        "name" : name,
        "rab1" : rab1,
        "rab2" : rab2,
        "rab3" : rab3,
        "rab4" : rab4,
    }

    return render(request, "about.html", context)


def contact(request):
    text_head = "Contact"
    name = "OOO Kamoliddin online book shop"
    address = "Alisher Navoiy 204/1"
    tel = "99-888-77-66"
    email = "kamoliddinnasirov@mail.ru"
    context = {
        "text_head" : text_head,
        "name" : name,
        "address" : address,
        "tel" : tel,
        "email" : email,
    }

    return render(request, "contact.html", context)





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
    # count input users
    num_visits = request.session.get("num_visits", 0)
    request.session['num_visits'] = num_visits + 1
    context = {
        "text_head" : text_head, 
        "books" : books,
        "num_books" : num_books,
        "num_instances" : num_instances,
        "num_instances_available" : num_instances_available,
        "authors" : authors,
        "num_authors" : num_authors,
        "num_visits" : num_visits,
    }

    return render(request, 'index.html', context)



