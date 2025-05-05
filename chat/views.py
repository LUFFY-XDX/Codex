from django.shortcuts import render
from django.http import HttpResponse
import requests
from django.views.decorators.csrf import csrf_exempt

# View for the chat page (Frontend)
def chat_page(request):
    return render(request, 'chat/chat.html')  # Ensure this template exists

# API for Chat functionality (returns plain text now)
@csrf_exempt
def chat_api(request):
    if request.method == 'POST':
        user_message = request.POST.get('user_message')
        if user_message:
            api_url = f"https://coderx-api-a3hd.onrender.com/chat?prompt={user_message}"
            try:
                response = requests.get(api_url)
                if response.status_code == 200:
                    data = response.json()
                    ai_response = data.get('response', "I couldn't process your request.")
                else:
                    ai_response = 'Error: AI API did not respond properly.'
            except Exception as e:
                ai_response = f"Exception occurred: {str(e)}"
            return HttpResponse(ai_response)
    return HttpResponse("Invalid request", status=400)
