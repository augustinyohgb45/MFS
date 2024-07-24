from django.shortcuts import render, redirect
from .forms import ChangementForm, IncidentForm, ITMFSForm, LoginForm
from django.contrib.auth import authenticate, login

def changement_view(request):
    if request.method == 'POST':
        form = ChangementForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ChangementForm()
    return render(request, 'changement.html', {'form': form})

def incident_view(request):
    if request.method == 'POST':
        form = IncidentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = IncidentForm()
    return render(request, 'incident.html', {'form': form})

def inscription_view(request):
    if request.method == 'POST':
        form = ITMFSForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = ITMFSForm()
    return render(request, 'inscription.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def home_view(request):
    return render(request, 'home.html')