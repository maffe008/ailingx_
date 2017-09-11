from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from ailingx.core.forms import SignUpForm
from ailingx.core.models import Area



@login_required
def home(request):
    curuser = request.user
    cells = curuser.cell_set.all()
    return render(request, 'home.html', {'curuser': curuser, 'cells': cells})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def index(request):
    return render(request, 'index.html')


def usecase(request):
    areas = Area.objects.all()
    return render(request, 'usecase.html', {'areas': areas})


def feature(request):
    return render(request, 'feature.html')


def blog(request):
    return render(request, 'blog.html')


def team(request):
    return render(request, 'team.html')


def joinus(request):
    return render(request, 'joinus.html')


def contact(request):
    return render(request, 'contact.html')
