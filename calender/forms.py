from django import forms
from django.forms import Textarea
from .models import Comment

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        # unique_together = ('post', 'user',)
        fields = ('text',)
        widgets = {
            'text': Textarea(attrs={'cols': 70, 'rows': 2}),
        }