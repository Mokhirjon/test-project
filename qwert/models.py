from django.db import models
from datetime import datetime
# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=30,default='')
    pub_date = models.DateTimeField(default=datetime.now)
    def __str__(self) ->str:
        return self.question_text
class Choice(models.Model) :
    Choice_text = models.CharField(max_lengh=200)
    votest = models.IntegerField(default=0)
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    def __str__(self) ->str:
        return self.question.question_text
