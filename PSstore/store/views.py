from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, CreateView
from .forms import *


class Main(TemplateView):
    template_name = "store/base.html"

class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'store/regist.html'

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))

class Login(LoginView):
    form_class = LoginUserForm
    template_name = 'store/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        return dict(list(context.items()))
    def get_success_url(self):
        return reverse_lazy('main')

def test(request):
    form = TestForm
    model = TestModel()
    if request.method == 'POST':
        print(request.POST.get('name'))
        print(request.POST.get('data'))
        model.name = request.POST.get('name')
        model.date = request.POST.get('data')
        model.save()

    return render(request, "store/test.html")

def logout_use(request):
    logout(request)
    return redirect('login')


def main(request):
    return render( request, "store/base.html" )