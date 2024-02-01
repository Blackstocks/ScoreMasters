from django.db import models
from customUser.models import CustomUser, Participant, Judge
from jsonfield import JSONField
from django.utils import timezone
from django.core.exceptions import ValidationError
import json

default_parameters = json.dumps({'p1': 0, 'p2': 0, 'p3': 0, 'p4': 0, 'p5': 0, 'p6': 0, 'p7': 0, 'p8': 0, 'p9': 0, 'p10': 0})

class Score(models.Model):
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE, null=True)
    judge = models.ForeignKey(Judge, on_delete=models.CASCADE, null=True)
    parameters = JSONField(null=True, default=default_parameters)
    total = models.FloatField(default=None)
    # status = models.BooleanField(default=False)

    class Meta:
        unique_together = (('participant', 'judge'),)

    def __str__(self):
        return f"{self.participant}, {self.judge}"

    def save(self, *args, **kwargs):
        # if not self.status:
            # Convert parameters to dictionary if it's stored as a string
            if isinstance(self.parameters, str):
                self.parameters = json.loads(self.parameters)

            # Calculate the total based on the values in the parameters field
            self.total = sum(self.parameters.values())

            super().save(*args, **kwargs)
        
        # else:
            # raise ValidationError("No multiple modifications in score is allowed.")

