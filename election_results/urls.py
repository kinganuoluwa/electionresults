from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", LoginView.as_view(template_name = 'login.html'), name='login'),
    path("logout", LogoutView.as_view(template_name = 'logout.html'), name='logout'),
    path("", include('results.urls')),
]
