from django.urls import path
from . import views

urlpatterns = [
    # path('results', views.results, name='results'),
    # path('add-results', views.ResultCreateView.as_view(), name='add-results'),
    path('wards/', views.WardListView.as_view(), name='ward_list'),
    path('wards/<int:pk>/', views.ward_detail, name='ward_detail'),
]