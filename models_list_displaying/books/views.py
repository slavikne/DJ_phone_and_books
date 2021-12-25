from django.shortcuts import render
from .models import Book

def books_view(request):
    books = Book.objects.all()
    template = 'books/books_list.html'
    context = {'books': books}
    return render(request, template, context)


def filtre_date(request,pub_date):
    date = pub_date
    books = Book.objects.filter(pub_date=date)
    book_big = Book.objects.filter(pub_date__gt=date).order_by('pub_date')[:1]
    book_small = Book.objects.filter(pub_date__lt=date).order_by('-pub_date')[:1]
    template = 'books/book_date.html'
    context = {'books': books,
               'book_big': book_big,
               'book_small': book_small}

    return render(request, template, context)