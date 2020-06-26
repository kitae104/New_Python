from django.forms import ModelForm
from tutorial.community.models import *

class Form(ModelForm):
    class Meta:
        model = Article
        fields = ['name', 'title', 'contents', 'url', 'email']