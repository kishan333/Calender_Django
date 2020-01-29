from rest_framework import viewsets
from .models import Event
from .serializers import eventSerializer

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = eventSerializer