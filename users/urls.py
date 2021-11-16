from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from questions.views import register_user

urlpatterns = [
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('register/', register_user, name='register'),
    path('password_change/', PasswordChangeView.as_view(
        template_name='users/password_change.html'), name='password_change'),
    path('password_change/done/', PasswordChangeDoneView.as_view(
        template_name='users/password_change_done.html'), name='password_change_done'),
]
