from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.base import ContextMixin
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import UserSession

# Create your views here.
class HomepageView(TemplateView):
  template_name = 'tracking/homepage.html'

  def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
    context = super().get_context_data(**kwargs)
    context.update({
      'user_sessions': UserSession.objects.filter(user=self.request.user),
    })
    return context

class RegisterView(TemplateView, ContextMixin):
  template_name = 'tracking/register.html'
  extra_context = {}

  def post(self, request):
    get = request.POST.get
    try:
      user = User.objects.create_user(
        username=get('username'),
        email=get('email'),
        password=get('password')
      )
      login(request, user)
      return redirect('/')

    except Exception as error:
      self.extra_context.update({
        'error': error,
      })
      return super().get(request)
      

class LoginView(TemplateView, ContextMixin):
  template_name = 'tracking/login.html'
  extra_context = {}

  def post(self, request):
    get = request.POST.get
    try:
      user = authenticate(
        request=request,
        username=get('username'),
        password=get('password'),
      )
      if user is not None:
        login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        return redirect('/')
      else:
        self.extra_context.update({'error':'The credentials passed for no user.'})
        return super().get(request)

    except Exception as error:
      self.extra_context.update({'error':error})
      return super().get(request)


def logout_view(request):
  logout(request)
  return redirect('/accounts/login/')