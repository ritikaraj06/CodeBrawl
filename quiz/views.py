from django.shortcuts import render

def homepage(request):
	return render(request, 'homepage.html')

def questions(request):
	return render(request, 'questions.html')

def quiz(request):
	return render(request, 'question.html')