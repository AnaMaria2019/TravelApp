from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView

from .views import *

urlpatterns = [
    path('login', LoginView.as_view(template_name='app/login_form.html'), name='user_login'),
    path('logout', LogoutView.as_view(), name='user_logout'),
    path('signup', SignUpView.as_view(), name='user_signup'),
    path('about', about, name='app_about'),
]
