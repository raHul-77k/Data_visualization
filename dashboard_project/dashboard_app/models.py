from django.db import models
from django.core.exceptions import ValidationError

class Data(models.Model):
    intensity = models.FloatField(default=0)
    likelihood = models.FloatField()
    relevance = models.FloatField()
    start_year = models.IntegerField(blank=True, null=True)
    end_year = models.IntegerField(blank=True, null=True, default=0)
    country = models.CharField(max_length=255, blank=True, null=True)
    topic= models.CharField(max_length=255, blank=True, null=True)
    region = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.topic

    def clean(self):
        super().clean()
        if not isinstance(self.intensity, (int, float)):
            raise ValidationError("Intensity must be a number")

    def save(self, *args, **kwargs):
        self.full_clean()
        if not self.end_year:
            self.end_year = 0
        super().save(*args, **kwargs)

