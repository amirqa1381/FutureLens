from django.urls import path
from .views import UserRegisterView, UserLoginView, logout_view
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path("register/", UserRegisterView.as_view(), name="user_register_view"),
    path("login/", UserLoginView.as_view(), name="user_login_view"),
    # path("logout/", LogoutView.as_view(template_name="account/logout.html"), name="logout_view"),
    path("logout/", logout_view, name="logout_view")
]
