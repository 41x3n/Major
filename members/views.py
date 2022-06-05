from .models import Member
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import IsAuthenticated
from .serializers import MemberSerializer


class MemberList(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Member.objects.all()
    serializer_class = MemberSerializer


class MemberDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
