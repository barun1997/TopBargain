from django.urls import path
from accounts.views import LoginView, RegisterView, LogoutView

urlpatterns = [
    path('login/', LoginView.as_view()),
    path('register/', RegisterView.as_view()),
    path('logout/', LogoutView.as_view)
]