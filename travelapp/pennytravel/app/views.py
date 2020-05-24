from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm  # It's a form for creating users, which comes with Django.
from django.urls import reverse_lazy

# Create your views here.


def welcome(request):
    return render(request, 'app/home_welcome.html')


def about(request):
    return render(request, 'app/about.html')


class SignUpView(CreateView):  # 'CreateView' is a generic class view that uses a form to create, validate and save
    # new model objects.
    form_class = UserCreationForm
    template_name = "app/signup_form.html"
    success_url = reverse_lazy('app_welcome')
