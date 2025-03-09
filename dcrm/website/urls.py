from django.urls import path
from . import views
from .models import Artist

# path('', views., name=''),

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('artists/', views.artists, name='artists'),
    path('artist/<str:pk>', views.artist_profile, name='artist_profile'),
    path('art/', views.art, name='art'),
    path('artwork/<str:pk>', views.artwork_profile, name='artwork_profile')
]
