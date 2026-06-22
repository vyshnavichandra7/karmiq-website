from django.shortcuts import render, redirect
from .models import Message
from users.models import User

def chat(request, receiver_id):
    sender_id = request.session.get('user_id')

    if not sender_id:
        return redirect('login')

    # send message
    if request.method == "POST":
        Message.objects.create(
            sender_id=sender_id,
            receiver_id=receiver_id,
            text=request.POST['text']
        )

    # fetch messages
    messages = Message.objects.filter(
        sender_id__in=[sender_id, receiver_id],
        receiver_id__in=[sender_id, receiver_id]
    ).order_by('timestamp')

    receiver = User.objects.get(id=receiver_id)

    return render(request, 'chat.html', {
        'messages': messages,
        'receiver': receiver,
        'sender_id': sender_id
    })