from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
# Create your views here.

def index(request):
    return HttpResponse("Hello World")

def book_by_id(request, book_id):
    book = Book.objects.get(pk=book_id)
    #return HttpResponse("Book: "+book.title+" Published on: "+book.pub_date)
    return render(request, "book_details.html",{"book":book})

def books(request):
    books = Book.objects.all()
    return render(request, "book_details.html",{"books":books})