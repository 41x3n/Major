from django.urls import path
from .views import MemberList, MemberDetail

urlpatterns = [
    path("", MemberList.as_view()),
    path("<int:pk>", MemberDetail.as_view()),
]
