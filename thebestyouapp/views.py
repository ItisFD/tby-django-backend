# views.py
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import UserProfile, UserLogin
from django.contrib.auth.hashers import make_password

@csrf_exempt
def create_profile_view(request):
    if request.method == 'POST':
        # Parse the request body to extract user profile and login data
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)

        # Create UserLogin object and save login information
        hashed_password = make_password(data['password'])
        user_login = UserLogin.objects.create(
            email=data['email'],
            password=hashed_password
        )

        # Create UserProfile object and associate it with the user login
        UserProfile.objects.create(
            user_login=user_login,
            age=data['age'],
            gender=data['gender'],
            height_inches=data['height_inches'],
            weight=data['weight'],
            target_weight=data['target_weight'],
            frequency=data['frequency'],
            level=data['level']
            # Add other fields as needed
        )
        return JsonResponse({'message': 'Profile created successfully'})
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)
