from django.shortcuts import render
from .models import Message
from .models import Chat

# Create your views here.
def index(request):
    if request.method == 'POST':
        print('Received message.' + request.POST['txtmsg'])
        myChat = Chat.objects.get(id=1)
        Message.objects.create(text = request.POST['txtmsg'], chat=myChat, author=request.user, receiver=request.user)
    return render(request, 'chat/index.html', {'username':'Raphael'})