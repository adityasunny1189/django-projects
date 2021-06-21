from django.shortcuts import render
from .models import Book
from django.db.models import Avg

# Create your views here.
def index(request):
	books = Book.objects.all()
	total_no_of_books = books.count()
	average_rating = books.aggregate(Avg('rating'))
	return render(request, 'book_outlet/index.html', {
			"books": books,
			"total_no_of_books": total_no_of_books, 
			"average_rating": average_rating 
		})

def book_detail(request, slug):
	book = Book.objects.get(slug=slug)
	return render(request, 'book_outlet/book_detail.html', {
			"author": book.author,
			"title": book.title,
			"rating": book.rating, 
			"is_bestselling": book.is_bestselling  
		})