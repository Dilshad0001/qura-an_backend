
from django.urls import path
from . import views

urlpatterns = [
    path('admin-login',views.AdminLoginView.as_view(), name='admin-login'),
    path('register/', views.AdminRegisterView.as_view(), name='admin-register'),
]
