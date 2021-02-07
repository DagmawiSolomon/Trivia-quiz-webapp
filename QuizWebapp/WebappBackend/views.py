from django.shortcuts import render
from .models import Quiz,Questions
# Create your views here.

def home(request):
    quiz = Quiz.objects.all()
    questions= Questions.objects.all()
    context = {"quiz":quiz}
    return render(request,"webappBackened/home.html",context)
