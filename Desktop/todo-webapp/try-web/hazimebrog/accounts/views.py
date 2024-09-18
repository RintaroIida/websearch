from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import CreateView

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import SignupForm

class SignupView(CreateView):
    model = User
    form_class = SignupForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('frontpage')

@login_required
def delete_account(request):
    if request.method == 'POST':
        request.user.delete()
        return redirect('frontpage')
    
    return render(request, 'accounts/delete_account.html')
# Create your views here.
