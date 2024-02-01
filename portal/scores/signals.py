from django.db.models.signals import post_save
from django.dispatch import receiver
from customUser.models import Judge, Participant
from .models import Score
from django.db import models
from django.dispatch import Signal
from django.db.models.signals import Signal

@receiver(post_save, sender=Judge)
def create_score_for_judge(sender, instance, created, **kwargs):
    if created:
        participants = Participant.objects.all()
        for participant in participants:
            Score.objects.get_or_create(participant=participant, judge=instance)

@receiver(post_save, sender=Participant)
def create_score_for_participant(sender, instance, created, **kwargs):
    if created:
        judges = Judge.objects.all()
        for judge in judges:
            Score.objects.get_or_create(participant=instance, judge=judge)

score_created = Signal()

# @receiver(post_save, sender=Score)
# def update_participant_total_score(sender, instance, **kwargs):
#     # participant = instance.participant

#     # # Calculate the average score based on associated scores
#     # non_zero_scores = Score.objects.filter(participant=participant, total__gt=0)
#     # # total_score = scores.aggregate(total=models.Sum('total'))['total']

#     # num_judges = non_zero_scores.count()
#     # if num_judges > 0:
#     #     total_score = sum(score.total for score in non_zero_scores)
#     #     average_score = total_score / num_judges
#     # else:
#     #     average_score = 0

#     # participant.total_score = average_score
#     # participant.save()

#     participant = instance.participant

#     # Get non-zero scores assigned to the participant
#     non_zero_scores = Score.objects.filter(participant=participant, total__gt=0).values_list('total', flat=True)

#     # Exclude judges who gave zero scores from the total judges count
#     total_judges = Score.objects.filter(participant=participant, total__gt=0).values('judge').distinct().count()
#     print(10)

#     if non_zero_scores:
#         average_score = sum(non_zero_scores) / total_judges if total_judges > 0 else 0
#     else:
#         average_score = 0

#     participant.total_score = average_score
#     participant.save()







@receiver(post_save, sender=Score)
def assign_rank_to_participant(sender, instance, **kwargs):
    participants = Participant.objects.all()

    # Filter participants based on the judge's panel_id
    # participants = participants.filter(score__judge__user=instance.judge.user)

    # participants_panel1 = Participant.objects.filter(rank__gt=0, panel_id=1)
    # participants_panel2 = Participant.objects.filter(rank__gt=0, panel_id=2)
    # # Sort participants based on total score
    # sorted_participants1 = sorted(participants_panel1, key=lambda p: p.total_score or 0, reverse=True)
    # sorted_participants2 = sorted(participants_panel2, key=lambda p: p.total_score or 0, reverse=True)
    # print(sorted_participants1)
    # for index, participant in enumerate(sorted_participants1):
    #     participant.rank = index + 1
    #     participant.save()

    participants_panel = participants.filter(score__judge__user=instance.judge.user)

    # Sort participants based on total score
    sorted_participants = sorted(participants_panel, key=lambda p: p.total_score or 0, reverse=True)

    for index, participant in enumerate(sorted_participants):
        participant.rank = index + 1
        participant.save()



@receiver(score_created)
def handle_score_creation(sender, **kwargs):
    judge = kwargs['judge']
    participant = kwargs['participant']
    print("triger")
    Score.objects.get_or_create(judge=judge, participant=participant)