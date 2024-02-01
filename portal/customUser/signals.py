from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import Participant, Judge

User = get_user_model()

@receiver(pre_save, sender=User)
def check_user_role(sender, instance, **kwargs):
    try:
        user = User.objects.get(pk=instance.pk)
    except User.DoesNotExist:
        pass  # User is being created, no need to check role
    else:
        if user.is_participant != instance.is_participant or user.is_judge != instance.is_judge:
            # User role has been modified, delete existing participant or judge object
            if user.is_participant:
                Participant.objects.filter(user=user).delete()
            elif user.is_judge:
                Judge.objects.filter(user=user).delete()

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.is_participant:
            Participant.objects.create(user=instance)
        elif instance.is_judge:
            Judge.objects.create(user=instance)
    else:
        if instance.is_participant:
            Participant.objects.update_or_create(user=instance)
        elif instance.is_judge:
            Judge.objects.update_or_create(user=instance)
