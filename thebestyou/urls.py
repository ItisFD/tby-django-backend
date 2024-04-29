from django.urls import path
from django.contrib import admin
from thebestyouapp.views import create_profile_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create-profile/', create_profile_view, name='create_profile'),
]
