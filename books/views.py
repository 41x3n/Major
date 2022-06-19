from .models import Books, Collections
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import IsAuthenticated
from .serializers import BookSerializer, CollectionSerializer


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


class CollectionList(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Collections.objects.all()
    serializer_class = CollectionSerializer

    def perform_create(self, serializer):
        request = serializer.context["request"]
        # print(request)
        serializer.save(user_id=request.user)

    def get_queryset(self):
        user_id = self.request.user
        return Collections.objects.filter(user_id=user_id)


class CollectionDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Collections.objects.all()
    serializer_class = CollectionSerializer
