from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from customUser.decorators import judge_required
from django.conf import settings
from django.contrib import messages
from googleapiclient.discovery import build
from google.oauth2 import service_account
from django.shortcuts import get_object_or_404
from customUser.models import Participant, CustomUser, Judge
from scores.models import Score
import os
from django.dispatch import Signal
from scores.signals import score_created
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import logging
logger = logging.getLogger(__name__)
from .forms import usersForm
from django.db.models import Q
from customUser.models import Participant

def create_score(judge, participant):
    score_created.send(sender=None, judge=judge, participant=participant)
    print("working!")

@judge_required
@login_required
# def dashboard(request):
    
#     return render(request, 'dashboardJudge/dashboard.html')

def dashboard(request):
    # Assuming you have some logic to determine the default panel_id
    default_panel_id = 1
    selected_panel_id = request.GET.get('panel_id', default_panel_id)

    context = {'selected_panel_id': selected_panel_id}
    return render(request, 'dashboardJudge/dashboard.html', context)


@judge_required
@login_required
def judge(request, participant_username):
    if not participant_username == "choose_participant":
        user = get_object_or_404(CustomUser, username= participant_username)
        participant = get_object_or_404(Participant, user=user)
        embed_link = participant.ppt_link
    
        # Trigger the score creation
        judge = request.user.judge  # Assuming the logged-in user is a judge
        create_score(judge, participant)
        print("judge working")
        
        return render(request, 'dashboardJudge/judging.html', {'embed_link': embed_link, 'participant_id': participant.user.id, 'judge_id': judge.user.id } )
    
    else:
        messages.success(request, 'Choose a participant')
        return redirect('judge_participants')

@judge_required
@login_required
# def leaderboard(request, panel_id=None):

#     if panel_id is None:
#         # Default to the first panel if no panel_id is provided
#         panel_id = 1
    

#     participants = Participant.objects.filter(rank__gt=0).order_by('rank')

#     participants = participants.filter(Q(scores__judge__panel_id=panel_id))
#     context = {'participants': participants}
#     return render(request, 'dashboardJudge/leaderboard.html', context)


def leaderboard(request, panel_id):

    if panel_id is None:
        # Default to the first panel if no panel_id is provided
        panel_id = 1

    # Assuming you have a field in the Judge model to indicate the panel/group (e.g., panel_id)

    participants_panel_1 = Participant.objects.filter(rank__gt=0, panel_id=1).order_by('rank')
    participants_panel_2 = Participant.objects.filter(rank__gt=0, panel_id=2).order_by('rank')

    context = {
        'participants_panel_1': participants_panel_1,
        'participants_panel_2': participants_panel_2,
    }
    return render(request, 'dashboardJudge/leaderboard.html', context)

    



@judge_required
@login_required
def participants(request):
    panel_id = request.user.judge.panel_id

    users = CustomUser.objects.filter(is_participant=True, participant__panel_id=panel_id).select_related('participant')
    return render(request, 'dashboardJudge/participants.html', {'users': users})


# @judge_required
# @login_required
# def create(response):
#     return render(response)

@judge_required
@login_required
# @csrf_exempt
def create_score_view(request, participant_id, judge_id):
    print(10)
    if request.method == 'POST':
        score_data = request.POST.dict()
        print(100)
        print(request)

        # Extract the parameter values from the score_data dictionary
        p1 = float(score_data.get('p1'))
        p2 = float(score_data.get('p2', 0))
        p3 = float(score_data.get('p3', 0))
        p4 = float(score_data.get('p4', 0))
        p5 = float(score_data.get('p5', 0))
        p6 = float(score_data.get('p6', 0))
        p7 = float(score_data.get('p7', 0))
        p8 = float(score_data.get('p8', 0))
        p9 = float(score_data.get('p9', 0))
        p10 = float(score_data.get('p10', 0))

        # Calculate the total score
        total_score = p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8 + p9 + p10

        # Get the participant and judge objects
        participant = Participant.objects.get(pk=participant_id)
        judge = Judge.objects.get(pk=judge_id)

        # Save the score to the database
        # score = Score(total=total_score, parameters={
        #     'p1': p1,
        #     'p2': p2,
        #     'p3': p3,
        #     'p4': p4,
        #     'p5': p5,
        #     'p6': p6,
        #     'p7': p7,
        #     'p8': p8,
        #     'p9': p9,
        #     'p10': p10
        # }, participant=participant, judge=judge)
        # score.save()


        existing_score = Score.objects.filter(participant=participant, judge=judge).first()

        if existing_score:
            # Update the existing score
            existing_score.total = total_score
            existing_score.parameters = {
                'p1': p1,
                'p2': p2,
                'p3': p3,
                'p4': p4,
                'p5': p5,
                'p6': p6,
                'p7': p7,
                'p8': p8,
                'p9': p9,
                'p10': p10
            }
            existing_score.save()
        else:
            # Create a new score
            score = Score(total=total_score, parameters={
                'p1': p1,
                'p2': p2,
                'p3': p3,
                'p4': p4,
                'p5': p5,
                'p6': p6,
                'p7': p7,
                'p8': p8,
                'p9': p9,
                'p10': p10
            }, participant=participant, judge=judge)
            score.save()

        print(total_score)  # Log the received data
    # Rest of your code...
        assign_rank_to_participant(participant.panel_id)
        


        return JsonResponse({'message': 'Score created successfully'})
    
    else:
        print(1000)
        return JsonResponse({'message': 'Invalid request method'})
    

# def userForm(request):
#     fn=usersForm()
#     data={'score':fn}
#     try:
#         if request.method=="POST":
#             p1=int(request.POST.get('p1'))
#             data ={
#                 'form': fn
#             }
#     except:
#         print("Error:!!")
    

def assign_rank_to_participant(panel_id):
    participants_panel = Participant.objects.filter(rank__gt=0, panel_id=panel_id).order_by('-total_score')

    for index, participant in enumerate(participants_panel):
        participant.rank = index + 1
        participant.save()