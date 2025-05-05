from django.shortcuts import render
from django.http import HttpResponse
import requests
from django.views.decorators.csrf import csrf_exempt
import markdown  # Markdown to HTML converter

def chat_page(request):
    return render(request, 'chat/chat.html')

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
                    # Convert markdown-like response to HTML
                    formatted_response = markdown.markdown(ai_response)
                else:
                    formatted_response = 'Error: AI API did not respond properly.'
            except Exception as e:
                formatted_response = f"<p><strong>Error:</strong> {str(e)}</p>"
            return HttpResponse(formatted_response)
    return HttpResponse("<p>Invalid request</p>", status=400)
