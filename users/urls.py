from django.urls import path, re_path
from dj_rest_auth.registration.views import RegisterView
from dj_rest_auth.views import LoginView, LogoutView

urlpatterns = [
    path("register/", RegisterView.as_view()),
    path("login/", LoginView.as_view()),
    path("logout/", LogoutView.as_view()),
]
