from django.urls import path
from . import views

urlpatterns=[
    path('book/<int:book_id>',views.book_by_id,name="book_by_id"),
    path('books/',views.books,name="books"),
    path('',views.home),
]