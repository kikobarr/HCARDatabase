from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .filters import ArtistFilter
from .models import *



def home(request):
    # corresponds with home.html <form method="POST" action="{% url 'home' %}">
    # if the action is POST
    if request.method == 'POST':
        # keys correspond to the name attribute in the form
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in.")
            return redirect('home')
        else:
            messages.success(request, "There was an error logging in.")
            return redirect('home')
    # else the action is GET, so we just serve the home page
    else:
        # myFilter = ArtistFilter()
        # artist_fname = Artist.artist_fname
        # artist_lname = Artist.artist_lname
        # context = {'artist_fname':artist_fname, 'artist_lname':artist_lname, 'myFilter':myFilter}
        # print(request.GET)
        # Django ORM database query
        # https://docs.djangoproject.com/en/5.1/topics/db/queries/
        # Entry.objects.filter(pub_date__year=2006)
        # Artist.objects.all()
        # if we have a search param,
        return render(request, 'home.html', {'foo':'bar'})


# note: function is called login_user so that it doesn't conflict with imported functions
def login_user(request):
    pass


def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('home')


def artists(request):
    artists = Artist.objects.all()
    return render(request, 'artists.html', {'artists': artists})
    return redirect('artists')


