from django.urls import path
from . import views

urlpatterns = [
    path('results', views.results, name='results'),
    path('add-results', views.ResultCreateView.as_view(), name='add-results'),
    path('polls', views.polls, name='polls'),
]