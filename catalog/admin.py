from django.contrib import admin
from catalog.models import *


admin.site.register(Author)
admin.site.register(Book)
admin.site.register(BookInstance)
admin.site.register(Genre)
admin.site.register(Status)
admin.site.register(Language)
admin.site.register(Publisher)


