import datetime
from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import User

class Event(models.Model):
	event_name = models.CharField(max_length=100)
	event_description = models.CharField(max_length=300)
	start_date = models.DateField(default=timezone.now)
	due_date = models.DateField(default=timezone.now)