from django.shortcuts import render
from catalog.models import Genre, Author ,Book, BookInstance
# Create your views here.
def index(request):
    """ View Function for Home page of the site """
    # Generates count of some of the main objects
    num_books       = Book.objects.all().count()
    num_instances   = BookInstance.objects.all().count()

    # Available Books ('status='a')
    num_instances_available     = BookInstance.objects.filter(status__exact='a').count()
    #number of author
    num_author      =Author.objects.count()

    return render()
