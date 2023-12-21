from django.contrib import admin
from catalog.models import Author, Book, BookInstance, Genre, Language, \
                                Publisher, Status
from django.utils.html import format_html

from django.utils.safestring import mark_safe

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth',  "show_photo")
    list_display_links = ('first_name', "last_name")
    fields = ['last_name', 'first_name', ('date_of_birth', 'photo')]
    readonly_fields = ['show_photo']
    def show_photo(self, obj):
        # return format_html(f"<img src='{obj.photo.url}' style='max-height: 100px'>")
        return mark_safe(f"<img src='{obj.photo.url}' style='max-height: 100px;'>")
    # show_photo.short_desctiption = "Photo"
    show_photo.short_desctiption = "Photo"


class BooksInstanceInline(admin.TabularInline):
    model = BookInstance

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "genre", "language", "display_author", "show_photo")
    list_filter = ("genre", "authors")
    inlines = [BooksInstanceInline]
    readonly_fields = ['show_photo']
    def show_photo(self, obj):
        return mark_safe(f"<img src='{obj.photo.url}' style='max-height: 100px;'>")
    show_photo.short_desctiption = "Muqova"






@admin.register(BookInstance)
class BookInstance(admin.ModelAdmin):
    list_display = ('book', 'status', 'customer', 'due_back', 'id')
    list_filter = ("book", "status")
    fieldsets = (
        ("Example book", {
            "fields" : ("book", "inv_nom")}),
        ("Status end book", {
            "fields" : ("status", "due_back", 'customer'),
        }

        )
    ) 






admin.site.register(Genre)
admin.site.register(Status)
admin.site.register(Language)
admin.site.register(Publisher)


