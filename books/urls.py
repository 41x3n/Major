from django.urls import path
from .views import BookList, BookDetail

urlpatterns = [
    path("", BookList.as_view()),
    path("<int:key>", BookDetail.as_view()),
]
