from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import requests



def home(request):
  all = request.GET.get('all')
  url = f'https://imdb-api.com/en/API/SearchAll/k_54v7k1ut/{all}'
  response = requests.get(url)
  data = response.json()
  items = data
  return render(request, 'home.html', {'items': items})


def top250_data(request):
  url = 'https://imdb-api.com/API/Top250Movies/k_54v7k1ut'
  response = requests.get(url)
  data = response.json()
  items = data['items']
  return render(request, 'top250_data.html', {'items': items})

def most_popular_data(request):
  url = 'https://imdb-api.com/en/API/MostPopularMovies/k_54v7k1ut'
  response = requests.get(url)
  data = response.json()
  items = data['items']
  return render(request, 'most_popular_data.html', {'items': items})

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('/')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)
