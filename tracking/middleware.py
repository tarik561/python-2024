from django.utils.deprecation import MiddlewareMixin
from django.utils import timezone
from .models import UserSession

# Create your middleware here
class UserSessionMiddleware(MiddlewareMixin):

    def process_request(self, request):
        if request.user.is_authenticated:
            session_key = request.session.session_key
            now = timezone.now()
            user_session, created = UserSession.objects.get_or_create(
                user=request.user,
                session_key=session_key,
                defaults={'last_activity': now}
            )
            if not created:
                user_session.last_activity = now
                user_session.save()

    def process_response(self, request, response):
        if request.user.is_authenticated and hasattr(request, 'session'):
            session_key = request.session.session_key
            now = timezone.now()
            UserSession.objects.filter(user=request.user, session_key=session_key).update(last_activity=now)
        return response
