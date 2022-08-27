from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView
from .admin import UserCreationForm
from .models import *
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, template_name='base.html')


def profile(request, pk):
    if request.user.is_authenticated:
        pk = request.user.pk
        my_user = get_object_or_404(MyUser, pk=pk)
        return render(request, template_name='accounts/profile.html', context={'user': my_user})
    else:
        messages = 'No authenticated User'
        return render(request, 'base.html', context={'messages': messages})


def my_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('accounts:home'))
        else:
            # Return an 'invalid login' error message.
            messages = 'invalid login'
            return render(request, 'registration/login.html', {'messages': messages})
    else:
        return render(request, 'registration/login_f.html')


@login_required
def logout_f(request):
    logout(request)
    return HttpResponseRedirect(reverse('accounts:home'))


# Sign Up View
class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login_view')
    template_name = 'registration/signup.html'


def register(request):
    if request.method == 'POST':
        print(request.POST)
        form = UserCreationForm(request.POST, files=request.FILES)
        if form.is_valid():
            user = form.save()
            user.save()
            return redirect('accounts:login')
            pass
        else:
            print('No valid')
            pass
        print(form.__dict__)
    else:
        pass
    return render(request, template_name='registration/signup_f.html')
