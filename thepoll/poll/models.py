from django.db import models
from django.conf import settings
from django.db.models import Sum 

# Create your models here.

class User(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.email  
      

class Poll(models.Model):
    voting_type = models.CharField(max_length=50)
    description = models.CharField(max_length=50, default="Who are you voting for?")
    pub_date = models.DateTimeField('date published')

    @property
    def total_votes(self):
        return self.choice_set.aggregate(total=Sum('votes'))['total'] or 0

    def __str__(self):
        return self.volting_types


class Choice(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=70)
    votes = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.choice_text
    

class Vote(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    voted_at = models.DateTimeField(auto_now_add=True)
