from django.contrib import admin
from .models import Message
from .models import Chat

class MessageAdmin(admin.ModelAdmin):
    fields = ('chat','text','created_at','author','receiver')
    list_display = ('text','created_at','author','receiver')
    search_fields = ('text',)

class ChatAdmin(admin.ModelAdmin):
    pass

# Register your models here.
admin.site.register(Message, MessageAdmin)
admin.site.register(Chat, ChatAdmin)