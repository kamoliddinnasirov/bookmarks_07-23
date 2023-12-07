from django.contrib import admin
from catalog.models import Author, Book, BookInstance, Genre, Language, \
                                Publisher, Status


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'photo')
    list_display_links = ('first_name', "last_name")
    fields = ['last_name', 'first_name', ('date_of_birth', 'photo')]


class BooksInstanceInline(admin.TabularInline):
    model = BookInstance

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "genre", "language", "display_author")
    list_filter = ("genre", "authors")
    inlines = [BooksInstanceInline]






@admin.register(BookInstance)
class BookInstance(admin.ModelAdmin):
    list_filter = ("book", "status")
    fieldsets = (
        ("Example book", {
            "fields" : ("book", "inv_nom")}),
        ("Status end book", {
            "fields" : ("status", "due_back"),
        }

        )
    ) 






admin.site.register(Genre)
admin.site.register(Status)
admin.site.register(Language)
admin.site.register(Publisher)


