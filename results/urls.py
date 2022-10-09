from django.urls import path
from . import views

urlpatterns = [
    path('results', views.results, name='results'),
    path('add-results', views.ResultCreateView.as_view(), name='add-results'),
    path('agents', views.AgentListView.as_view(), name='agents'),
]