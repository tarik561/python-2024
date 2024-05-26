from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import HomepageView, LoginView, RegisterView, logout_view

urlpatterns = [
    path('', login_required(HomepageView.as_view()), name='homepage'),
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('accounts/register/', RegisterView.as_view(), name='register'),
    path('accounts/logout/', logout_view, name='logout'),
]
