from django.urls import path
from .views import BookList, BookDetail, CollectionList, CollectionDetail

urlpatterns = [
    path("collection", CollectionList.as_view()),
    # path("collection/<int:book_id>", CollectionDetail.as_view()),
    path("", BookList.as_view()),
    path("<int:key>", BookDetail.as_view()),
]
