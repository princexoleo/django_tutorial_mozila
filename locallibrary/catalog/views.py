from django.shortcuts import render
from django.views import generic
from django.shortcuts import get_object_or_404
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

class BookListView(generic.ListView):
    model = Book
    def get_queryset(self):
        return Book.objects.filter(title__icontains='The')[:5]# Get 5 books containing the title war
    
    def get_context_data(self, **kwargs):
        context = super(BookListView, self).get_context_data(**kwargs)# Call the base implementation first to get the context
        context["some_data"] = 'This is some data inserted' 
        return context
    

class BookDetailView(generic.DetailView):
    model = Book 

    def book_detail_view(request, primary_key):
        try:
            book = Book.objects.get(pk=primary_key)
        except Book.DoesNotExist:
            raise Http404('Book does not exist')
        return render(request, 'catalog/book_detail.html', context={'book': book})


