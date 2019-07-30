from django.contrib import admin
from catalog.models import Book,BookInstance,Author,Genre,Language

 #Define the admin class
class AuthorAdmin(admin.ModelAdmin):
    list_display  = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields        = ['first_name', 'last_name', ('date_of_birth','date_of_death')] 

# Register the admin class with the associated model
admin.site.register(Author,AuthorAdmin)


# Decorate admin.site.register
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre') #display_genre is custom function


# BookInstance and BookInstance Admin
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')

    fieldsets = (
        (None, {
            "fields": (
                'book',
                'imprint',
                'id'
            ),
        }),
        ('Availability',{
            'fields':('status','due_back')
        }),
    )
    
    


# # Register your models here.
# admin.site.register(Book)


admin.site.register(Genre)
#admin.site.register(BookInstance)
admin.site.register(Language)
