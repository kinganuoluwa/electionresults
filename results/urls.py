from django.urls import path
from . import views


app_name = "results"

urlpatterns = [
    path('', views.total_result, name='total_result'),
    path('wards/', views.WardListView.as_view(), name='ward_list'),
]
