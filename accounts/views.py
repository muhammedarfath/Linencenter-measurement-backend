
import json
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.middleware.csrf import get_token
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

@csrf_exempt
@require_POST
def login_view(request):
    data = json.loads(request.body)
    email = data.get('email')
    password = data.get('password')

    user = authenticate(request, username=email, password=password)

    if user is not None:
        login(request, user)
        response = JsonResponse({'message': 'Login successful'})
        response.set_cookie('csrftoken', get_token(request), httponly=True)
        return response
    else:
        return JsonResponse({'error': 'Invalid email or password'}, status=400)
