from django.urls import  path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("books/", views.BookListView.as_view(), name="books"),
    path("books/<int:pk>/", views.BookDetailView.as_view(), name="book-detail"),
    
    path("authors/", views.AuthorListView.as_view(), name="authors-list"),
    path("authors/<int:pk>/", views.AuthorDetailView.as_view(), name="author-detail"),
    
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("mybooks/", views.LoanedBooksByUserListView.as_view(), name="my-borrowed"),
    path("edit_authors/", views.edit_author, name="edit_authors"),
    path("authors_add/", views.add_author, name="authors_add"),
    path("delete/<int:id>", views.delete, name='delete'),
    path("edit_author/<int:id>", views.edit_author, name="edit_author"),
    path("edit_books/", views.edit_books, name="edit_books"),

    path("book/create/", views.BookCreate.as_view(), name="book_create"),
    path("book/update/<int:pk>", views.BookUpdate.as_view(), name="book_update"),
    path("book/delete/<int:pk>", views.BookDelete.as_view(), name="book_delete"),
    
]