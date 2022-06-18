from .models import Books
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import IsAuthenticated
from .serializers import BookSerializer


class BookList(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Books.objects.all()
    serializer_class = BookSerializer

    def perform_create(self, serializer):
        request = serializer.context["request"]
        print(request)
        serializer.save(added_by_user=request.user)


class BookDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Books.objects.all()
    serializer_class = BookSerializer
