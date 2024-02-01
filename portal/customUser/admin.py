from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Participant, Judge
import os
from django.conf import settings
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

class CustomUserAdmin(UserAdmin):
    fieldsets = list(UserAdmin.fieldsets)
    fieldsets[0] = (None, {'fields': ('username', 'password', 'is_judge', 'is_participant')})
    UserAdmin.fieldsets = tuple(fieldsets)

    list_filter = list(UserAdmin.list_filter)
    list_filter.append('is_judge')
    UserAdmin.list_filter = tuple(list_filter)

    list_display = ('username','first_name', 'last_name', 'is_judge', 'email')

class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('user', 'total_score', 'rank')
    list_filter = ('rank',)
    ordering = ('rank',)

admin.site.register(Participant, ParticipantAdmin)

admin.site.register(Judge)

admin.site.register(CustomUser, CustomUserAdmin)
