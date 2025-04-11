"""
Expected classes:
    - Workout
        - wo_type: strfield
        - wo_duration: intfield
        - wo_date: datetimefield
        - wo_intensity: intfield
        - wo_set_qty: intfield
        - wo_qty_of_set: intfield
"""
from django.db import models


class Workout(models.Model):
    wo_date = models.DateTimeField("workout date", auto_now_add=True)
    wo_type = models.CharField("workout type", max_length=50)
    wo_intensity = models.IntegerField("workout intensity")
    wo_set_qty = models.IntegerField("workout set quantity")
    wo_qty_of_set = models.IntegerField("workout quantity of set")
    wo_duration = models.IntegerField("workout duration")

    def __str__(self):
        return f"{self.wo_type} | {self.wo_duration} | {self.wo_date.strftime('%Y-%m-%d')}min"
