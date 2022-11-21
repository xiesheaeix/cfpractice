from django.urls import path
from .import views

urlpatterns = [
    path('accounts/signup/', views.signup, name='signup'),
    path('', views.home, name='home'),
    path('top250_data', views.top250_data, name='top250_data'),
    path('most_popular_data', views.most_popular_data, name='most_popular_data'),
]