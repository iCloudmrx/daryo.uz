from django.urls import path
from .views import *


urlpatterns = [
    # ex: localhost
    path('', post_list, name='post_list'),
    # ex: localhost/year/month/day/slug
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
         post_detail, name='post_detail'),
]
