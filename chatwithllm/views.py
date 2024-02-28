from django.shortcuts import render
from .models import Message
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from .model_response import llm_obj

def chat_view(request):
    global model, tokenizer
    if request.method == 'POST':
        username = request.POST.get('username')
        message = request.POST.get('message')
        Message.objects.create(username=username, message=message)

        system_message = llm_obj.response(message)
        Message.objects.create(username="System", message=system_message, is_user=False)

        # Redirect to avoid form resubmission on refresh
        return HttpResponseRedirect('/chatwithllm')
    else:
        messages = Message.objects.all()
        return render(request, 'chat.html', {'messages': messages})

def clear_chat(request):
    if request.method == 'POST':
        # Clear all chat messages
        Message.objects.all().delete()
        # Redirect back to chat view
        return redirect('chat')