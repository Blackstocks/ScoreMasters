from django.contrib import admin
from django import forms
from .models import Score

class ScoreAdmin(admin.ModelAdmin):
    list_display = ('participant','judge', 'total',)

    class Meta:
        model = Score
        fields = '__all__'

admin.site.register(Score, ScoreAdmin)
# Register your models here.
