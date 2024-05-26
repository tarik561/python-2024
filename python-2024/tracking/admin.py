from django.contrib import admin
from .models import UserSession

class UserSessionAdmin(admin.ModelAdmin):
    list_display = ('user', 'session_key', 'login_time', 'last_activity', 'logout_time')
    list_filter = ('user', 'login_time', 'last_activity', 'logout_time')
    search_fields = ('user__username', 'session_key')


admin.site.register(UserSession, UserSessionAdmin)
