from django.shortcuts import render
from catalog.models import Genre, Author ,Book, BookInstance
# Create your views here.
def index(request):
    """ View Function for Home page of the site """
    # Generates count of some of the main objects
    num_books       = Book.objects.all().count()
    num_instances   = BookInstance.objects.all().count()

    # Available Books ('status='a')
    num_instances_available    = BookInstance.objects.filter(status__exact='a').count()
    #number of author
    num_authors      =   Author.objects.count()

    context = {
        'num_books' : num_books,
        'num_instances' : num_instances,
        'num_instance_available' : num_instances_available,
        'num_authors' : num_authors,
    }
    # Render the HTML templates index.html with the data in context variable
    return render(request, 'index.html', context=context)
