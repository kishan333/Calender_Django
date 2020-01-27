import datetime
from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import User

class Event(models.Model):
	event_name = models.CharField(max_length=100)
	event_description = models.TextField(default=True)
	created_date = models.DateTimeField(default=timezone.now)