from django.urls import path
from . import views


app_name = "results"

urlpatterns = [
    # path('results/', views.polling_result, name='polling_result'),
    path('results/total', views.total_result, name='total_result'),
    path('add-results', views.ResultCreateView.as_view(), name='add_results'),
    path('wards/', views.WardListView.as_view(), name='ward_list'),
    path('wards/<int:pk>/', views.ward_detail, name='ward_detail'),
]
