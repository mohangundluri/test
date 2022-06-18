from django.contrib import admin
from .models import FeedbackModel

class FeedabackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message', 'created_at', 'is_consent')
    

admin.site.register(FeedbackModel, FeedabackAdmin)
