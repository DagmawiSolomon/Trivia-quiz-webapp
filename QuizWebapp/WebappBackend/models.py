from django.conf import settings
from django.db import models

# Create your models here.


class Questions(models.Model):
    question = models.TextField()
    choice1 = models.CharField(max_length=100)
    choice2 = models.CharField(max_length=100)
    choice3 = models.CharField(max_length=100)
    choice4 = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)

    def __str__(self):
        return self.question


class Quiz(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    registered = models.BooleanField(default=False)
    start_date = models.DateField(null=True, blank=True)
    completed  = models.BooleanField(default=False)
    active = models.BooleanField(default=False)


    def __str__(self):
        return f"{self.question}({self.start_date})"




class User(models.Model):
    name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE )


