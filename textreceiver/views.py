from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import TextInput
import json

# home
def home(request):
    # Fetch all entries from the TextInput model
    entries = TextInput.objects.all()

    # Create a simple HTML response with the data
    response_content = "<h1>Received Data</h1><ul>"
    for entry in entries:
        response_content += f"<li>UserID: {entry.user_id}, Text: {entry.text}</li>"
    response_content += "</ul>"

    return HttpResponse(response_content)

@csrf_exempt
def receive_text(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_id = data.get('userID', '')
            text = data.get('text', '')
            
            # Save to the database
            TextInput.objects.create(user_id=user_id, text=text)

            # Respond with a confirmation message
            return JsonResponse({'message': f'User {user_id} sent: {text}'})
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
    return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)
