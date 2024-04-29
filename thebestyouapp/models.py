from django.db import models

class UserLogin(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

class UserProfile(models.Model):
    user_login = models.OneToOneField(UserLogin, on_delete=models.CASCADE)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    height_inches = models.IntegerField()
    weight = models.FloatField()
    target_weight = models.FloatField()
    frequency = models.CharField(max_length=50)
    level = models.CharField(max_length=50)
    # Add other fields as needed