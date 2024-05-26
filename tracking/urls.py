from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import HomepageView

urlpatterns = [
    path('', login_required(HomepageView.as_view())),
]
