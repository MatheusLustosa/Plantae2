from datetime import datetime
from django.db import models
from django.urls import reverse
from site_cc.models import EventAbstract
from accounts.models import User

class EventManager(models.Manager):
    """ Event manager """

    def get_all_events(self, user):
        events = Event.objects.filter(user=user, is_active=True, is_deleted=False)
        return events

    def get_running_events(self, user):
        running_events = Event.objects.filter(
            user=user,
            is_active=True,
            is_deleted=False,
            end_time__gte=datetime.now().date(),
        ).order_by("start_time")
        return running_events


class Event(EventAbstract):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="events")
    title = models.CharField(max_length=200)
    type = models.CharField(max_length=50, default='')  
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    objects = EventManager()

    def _str_(self):
        return self.title

    def get_absolute_url(self):
        return reverse("site_cc:event-detail", args=(self.id,))

    @property
    def get_html_url(self):
        url = reverse("site_cc:event-detail", args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'