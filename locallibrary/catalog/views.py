from django.shortcuts import render
from django.views import generic
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import permission_required
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


# Author ListView
class AuthorListView(generic.ListView):
    model = Author
    def get_queryset(self):
        return Author.objects.all()[:5] # get 5 authors list
    
    def get_context_data(self, **kwargs):
        context = super(AuthorListView, self).get_context_data(**kwargs) # Call the base implementation first to get the context
        context['some_data']    = 'This is some authors context data'
        return context

# Author Detail View
class AuthorDetailView(generic.DetailView):
    model = Author

    def author_detail_view(request, primary_key):
        try:
            author = Author.objects.get(pk=primary_key)
        except Author.DoesNotExist:
            raise Http404('Author Doesnot Exists')
        return render(request,'catalog/author_detail.html')
    
    

class LoanedBooksByUserListView(LoginRequiredMixin, generic.ListView):
    """Generic class-based view listing books on loan to current user."""
    model = BookInstance
    template_name ='catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 10
    
    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')


