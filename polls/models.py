from django.db import models

# Create your models here.

import datetime

from django.db import models
from django.utils import timezone


# question object
class Question(models.Model):
    # object/question properties
    # question_text and pub_date auto generate on admin page
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    # actions/methods taken by Question object
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    # object/choice properties
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
