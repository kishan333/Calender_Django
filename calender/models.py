import datetime
from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import User

class Event(models.Model):
	title = models.CharField(max_length=100)
	# event_description = models.CharField(max_length=300)
	start = models.DateField(default=timezone.now)
	end = models.DateField(default=timezone.now)