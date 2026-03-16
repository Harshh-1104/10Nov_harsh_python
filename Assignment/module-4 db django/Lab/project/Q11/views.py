from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm

def book_list(request):
    books = Book.objects.all()
    return render(request, 'Q11/book_list.html', {
        'books': books,
        'title': 'Q11 - Database Connectivity Demo',
    })

def book_add(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('q11_home')
    else:
        form = BookForm()
    return render(request, 'Q11/book_form.html', {'form': form})

