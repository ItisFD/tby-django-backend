from django.contrib import admin
from .models import UserProfile, UserLogin

# Define a custom admin class for UserProfile
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('email', 'password', 'age', 'gender', 'height_inches', 'weight', 'target_weight', 'frequency', 'level')
    search_fields = ['user_login__email']  # Update to search by email in UserLogin model

    # Define methods to fetch email and password from related UserLogin model
    def email(self, obj):
        return obj.user_login.email

    def password(self, obj):
        return obj.user_login.password

# Register the models with their respective admin classes
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(UserLogin)  # Register UserLogin as well if needed
