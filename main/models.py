from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime


class Event(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(
        'main.Category',
        on_delete=models.CASCADE
    )
    start_datetime = models.DateTimeField(null=True, blank=True)
    end_datetime = models.DateTimeField(null=True, blank=True)
    reg_due_datetime = models.DateTimeField(null=True, blank=True)
    virtual = models.BooleanField(default=False)
    description = models.TextField(max_length=1000)
    prog_mgr = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="prog_mgr")
    comm_lead = models.ManyToManyField(settings.AUTH_USER_MODEL)
    
    status_fk = models.ForeignKey(
        'main.Status',
        on_delete=models.CASCADE,
        default=''
    )

    img_url = models.CharField(max_length=5000)
    
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class EventPM(models.Model):
    PM_fk = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    event_fk = models.ForeignKey(
        'main.Event',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return str(self.PM_fk)

class EventCL(models.Model):
    CL_fk = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    event_fk = models.ForeignKey(
        'main.Event',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return str(self.CL_fk)

class Status(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Registration(models.Model):
    participant_fk = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    event_fk = models.ForeignKey(
        'main.Event',
        on_delete=models.CASCADE
    )
    status_fk = models.ForeignKey(
        'main.Status',
        on_delete=models.CASCADE,
        default=''
    )

    def __str__(self):
        return str(self.participant_fk) + " - " + str(self.event_fk)

class FeedbackPT(models.Model):
    participant_fk = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='participants'
    )
    event_fk = models.ForeignKey(
        'main.Event',
        on_delete=models.CASCADE
    )
    status_fk = models.ForeignKey(
        'main.Status',
        on_delete=models.CASCADE
    )
    
    description = models.TextField(max_length=1000, default='Not Set')
    # rating = models.IntegerField(validators=[MinValueValidator(1),
    #                                    MaxValueValidator(5)], null=True, blank=True)

    def __str__(self):
        return str(self.participant_fk) + " - " + str(self.event_fk)
