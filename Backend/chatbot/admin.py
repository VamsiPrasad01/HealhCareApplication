from django.contrib import admin
from .models import ChatMessage

@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ('user', 'message_preview', 'timestamp')
    list_filter = ('user', 'timestamp')
    search_fields = ('message', 'response')

    def message_preview(self, obj):
        return obj.message[:50]
    message_preview.short_description = 'Message'