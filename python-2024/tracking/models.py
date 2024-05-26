from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    session_key = models.CharField(max_length=40)
    login_time = models.DateTimeField(auto_now_add=True)
    last_activity = models.DateTimeField(auto_now=True)
    logout_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.user.username} - {self.session_key}'
