from django.contrib import admin
from .models import UserSession

# Register your models here.
class UserSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    session_key = models.CharField(max_length=40, unique=True)
    login_time = models.DateTimeField(auto_now_add=True)
    last_activity = models.DateTimeField(auto_now=True)
    logout_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.user.username} - {self.session_key}'


class UserSessionAdmin(admin.ModelAdmin):
    list_display = ('user', 'session_key', 'login_time', 'last_activity', 'logout_time')
    list_filter = ('user', 'login_time', 'last_activity', 'logout_time')
    search_fields = ('user__username', 'session_key')


admin.site.register(UserSession, UserSessionAdmin)
