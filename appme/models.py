from django.db import models
from django.contrib.auth.models import User


#مدل ذخیره ی یوزر جدید
class RegistrationRequest(models.Model):
    admin_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='registration_requests_made')
    new_username = models.CharField(max_length=150, unique=True)
    new_password = models.CharField(max_length=128)  # رمز عبور به صورت هش شده ذخیره می شود
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Request for {self.new_username} by {self.admin_user.username}"