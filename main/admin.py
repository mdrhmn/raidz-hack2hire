from django.contrib import admin
from .models import *

admin.site.register(Event)
admin.site.register(Registration)
admin.site.register(Status)
admin.site.register(Category)
admin.site.register(FeedbackPT)
admin.site.register(EventProposal)


@admin.register(EventPM)
class EventPM(admin.ModelAdmin):
    list_display = ('id', 'PM_fk', 'event_fk')
    list_filter = ('event_fk__name',)
    ordering = ("PM_fk",)

@admin.register(EventCL)
class EventCL(admin.ModelAdmin):
    list_display = ('id', 'CL_fk', 'event_fk')
    list_filter = ('event_fk__name',)
    ordering = ("CL_fk",)