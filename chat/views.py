from django.shortcuts import render
from django.http import JsonResponse
import requests
from django.views.decorators.csrf import csrf_exempt

# View for the chat page (Frontend)
def chat_page(request):
    return render(request, 'chat/chat.html')  # Make sure chat.html exists in your templates folder

# API for Chat functionality
@csrf_exempt
def chat_api(request):
    if request.method == 'POST':
        user_message = request.POST.get('user_message')
        if user_message:
            api_url = f"https://coderx-api-a3hd.onrender.com/chat?prompt={user_message}"
            response = requests.get(api_url)
            if response.status_code == 200:
                data = response.json()
                ai_response = data.get('response', "I couldn't process your request.")
            else:
                ai_response = 'Error connecting to the AI API.'
            return JsonResponse({'ai_response': ai_response})

    return JsonResponse({'error': 'Invalid request'}, status=400)
