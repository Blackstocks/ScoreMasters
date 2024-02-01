from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from customUser.decorators import participant_required
from django.conf import settings
from django.contrib import messages
from django.shortcuts import get_object_or_404
from customUser.models import Participant, CustomUser, Judge
from scores.models import Score
import os
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth.views import LoginView
from django.db.models import Max


@login_required
@participant_required
def dashboard(request):
    return render(request, 'dashboardParticipant/dashboard.html')

@login_required
@participant_required
def result(request):
    participant = request.user.participant  # Retrieve the currently logged-in participant
    participant_rank = participant.rank
    participant_score = participant.total_score
    top_score = top_score = Participant.objects.aggregate(max_score=Max('total_score'))['max_score']

    scores = Score.objects.filter(participant=participant)  # Query scores associated with the participant

    score_list = []  # List to store the judge's name and marks for each score
    for score in scores:
        judge_name = score.judge.user  # Assuming the judge model has a 'name' field
        marks_given = score.total
        score_list.append({'judge_name': judge_name, 'marks_given': marks_given})

    context = {
        'scores': score_list,
        'participant_rank': participant_rank,
        'participant_score': participant_score,
        'top_score': top_score,
    }

    return render(request, 'dashboardParticipant/result.html', context)

@login_required
@participant_required
def connect(request):
    judges = Judge.objects.all()
    context = {
        'judges': judges
    }
    return render(request, 'dashboardParticipant/connect.html', context)


@login_required
@participant_required
def leaderboard(request):
    participants = Participant.objects.filter(rank__gt=0).order_by('rank')
    context = {'participants': participants}
    return render(request, 'dashboardParticipant/leaderboard.html', context)

class CustomLoginView(LoginView):
    def get_success_url(self):
        return '/participant/dashboard/'
    
