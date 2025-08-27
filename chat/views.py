from django.shortcuts import render
from django.http import HttpResponse
import requests
from django.views.decorators.csrf import csrf_exempt
from django.utils.html import escape
from urllib.parse import quote_plus

# View for the chat frontend
def chat_page(request):
    return render(request, 'chat/chat.html')  # Assumes your template is at templates/chat/chat.html

# Chat API view (returns plain text instead of JSON)
@csrf_exempt
def chat_api(request):
    if request.method == 'POST':
        user_message = request.POST.get('user_message')
        if user_message:
            try:
                encoded_prompt = quote_plus(user_message)
                api_url = f"https://coderx-api-cgra.onrender.com/chat?prompt={encoded_prompt}"
                response = requests.get(api_url, timeout=35)
                if response.status_code == 200:
                    data = response.json()
                    ai_response = data.get('response', "No response received.")
                    return HttpResponse(escape(ai_response))  # Send plain text directly
                else:
                    return HttpResponse("AI API responded with an error.", status=502)
            except Exception as e:
                return HttpResponse(f"Something went wrong: {e}", status=500)
    return HttpResponse("Invalid request", status=400)
