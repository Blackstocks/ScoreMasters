from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from jsonfield import JSONField
from django.apps import apps
import os
import json

class CustomUser(AbstractUser):
    is_judge = models.BooleanField('judge status', blank=True, default=False)
    is_participant = models.BooleanField('participant status', blank=True, default=False)

class Participant(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    ppt_link = models.URLField(blank=True, max_length=1000)
    total_score = models.FloatField(null=True, default=0)
    rank = models.IntegerField(null=True, default=0)
    num_judges_with_zero = models.IntegerField(null=True, default=0)
    panel_id = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        if self.user.is_participant:
            Score = apps.get_model(app_label='scores', model_name='Score')
            scores = Score.objects.filter(participant=self)
            # total_score = scores.aggregate(total=models.Sum('total'))['total']
            # num_scores = scores.count()
            # average_score = total_score / num_scores if num_scores > 0 else 0
            # self.total_score = average_score
            non_zero_scores = scores.exclude(total=0)

            total_score = non_zero_scores.aggregate(total=models.Sum('total'))['total']
            num_scores = non_zero_scores.count()
            average_score = total_score / num_scores if num_scores > 0 else 0
            self.total_score = average_score
            print(average_score)


            super().save(*args, **kwargs)
        else:
            raise ValueError("Only participants are allowed.")

class Judge(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    startups_judged = JSONField(null=True, default={})
    total_startups_judged = models.IntegerField(null=True, default=0)
    panel_id = models.IntegerField()
    

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        # if self.user.is_judge:
        #     super().save(*args, **kwargs)
        # else:
        #     raise ValueError("Only judges are allowed.")
        super().save(*args, **kwargs)
