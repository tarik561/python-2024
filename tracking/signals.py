from django.contrib.auth.signals import user_logged_out
from django.dispatch import receiver
from django.utils import timezone
from .models import UserSession

# Create your signals here
@receiver(user_logged_out)
def update_logout_time(sender, request, user, **kwargs):
    session_key = request.session.session_key
    now = timezone.now()
    UserSession.objects.filter(user=user, session_key=session_key).update(logout_time=now)