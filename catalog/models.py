from django.db import models
from django.urls import reverse 




class Genre(models.Model):
    name = models.CharField(max_length=200,
                            help_text="Input genre",
                            verbose_name="Genre book")
    

    def __str__(self) -> str:
        return self.name 
    


class Language(models.Model):
    name = models.CharField(max_length=20,
                            help_text="Input language book",
                            verbose_name="Language book")
    
    def __str__(self) -> str:
        return self.name 
    



class Publisher(models.Model):
    name = models.CharField(max_length=20, 
                            help_text="Input name publisher",
                            verbose_name="Publisher book")
    
    def __str__(self) -> str:
        return self.name
    


class Author(models.Model):
    first_name = models.CharField(max_length=100,
                                  help_text="Input name author",
                                  verbose_name="First name author")
    
    last_name = models.CharField(max_length=100,
                                 help_text="Input last author",
                                 verbose_name="Last name author")
    
    date_of_birth = models.DateField(
        help_text="Input birthday",
        verbose_name="Birthday author",
        null=True, blank=True)
    
    about = models.TextField(help_text="Input about author", verbose_name="About author")
    photo = models.ImageField(upload_to="author/%Y/%m/%d")

    def __str__(self) -> str:
        return self.last_name
    
    
    

class Book(models.Model):
    title = models.CharField(max_length=200,
                             help_text="Input title book",
                             verbose_name="Book title")
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE,
                              help_text="Choice genre",
                              verbose_name="Genre book", null=True)
    language = models.ForeignKey("Language", on_delete=models.CASCADE,
                                 help_text='Choice lang',
                                 verbose_name="Lang book")
    publisher = models.ForeignKey("Publisher", on_delete=models.CASCADE, 
                                  help_text="Choice publisher",
                                  verbose_name='Publisher book')
    year = models.CharField(max_length=4,
                            help_text="Input year publications",
                            verbose_name="Year publications")

    authors = models.ManyToManyField('Author',
                                    help_text="Choice author book",
                                    verbose_name="Author(authors) book")

    summary = models.TextField(max_length=1000, help_text="Input short summary about book",
                               verbose_name="Annotation book")
    isbn = models.CharField(max_length=13, help_text="Input 13 syvols isbn",
                            verbose_name="Book isbn")

    price = models.DecimalField(decimal_places=2, max_digits=7,
                                help_text="Input price book",
                                verbose_name="Price book")

    photo = models.ImageField(upload_to="books/%Y/%m/%d",
                              help_text="Input image book",
                              verbose_name="Image book")

    def __str__(self) -> str:
        return self.title 


    def get_absolute_url(self):
        return reverse("book-detail", args=[str(self.id)])

    def display_author(self):
        return ', '.join([author.last_name for author in self.authors.all()])
    display_author.short_description = 'Authors'

class Status(models.Model):
    name = models.CharField(max_length=20,
                            help_text="Input status book",
                            verbose_name="Status book")
    
    def __str__(self) -> str:
        return self.name 
    


class BookInstance(models.Model):
    book = models.ForeignKey('Book', on_delete=models.CASCADE, null=True)

    inv_nom = models.CharField(max_length=20, null=True, help_text="Input inv number",
                               verbose_name="Inv number book")
    status = models.ForeignKey("Status", on_delete=models.CASCADE, null=True, 
                               help_text="Edit status book",
                               verbose_name="Status book")
    due_back = models.DateField(null=True, blank=True, help_text="Input end status",
                                verbose_name="Date end status")
    
    class Meta:
        ordering = ['due_back']

    def __str__(self) -> str:
        return '%s %s %s' % (self.inv_nom, self.book, self.status)


    
