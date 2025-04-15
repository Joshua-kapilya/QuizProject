from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.shortcuts import get_object_or_404
# Create your views here.

from django.shortcuts import render
from .models import Subject, PastPaper, Question



def get_explanation(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    return JsonResponse({"explanation": question.explanation1})

def home(request):
	return render(request, 'home.html')

def home(request):
    subjects = Subject.objects.all()
    return render(request, 'home.html', {'subjects': subjects})

def select_quiz_mode(request, subject_id):
    subject = Subject.objects.get(id=subject_id)
    past_papers = PastPaper.objects.all()
    return render(request, 'select_quiz_mode.html', {'subject': subject, 'past_papers': past_papers})

def get_questions(request, subject_id):
    past_paper_id = request.GET.get('past_paper_id')  # Get selected past paper (if any)

    if past_paper_id:
        questions = Question.objects.filter(subject_id=subject_id, past_paper_id=past_paper_id).order_by('question_number')
    else:
        questions = Question.objects.filter(subject_id=subject_id).order_by('question_number')

    return render(request, 'questions.html', {'questions': questions})




def check_answer(request):
    if request.method == "POST":
        data = json.loads(request.body)
        question_id = data.get("question_id")
        user_answer = data.get("answer_value")

        try:
            question = Question.objects.get(id=question_id)
            correct_answer = question.correct_answer  # Ensure correct_answer exists in the model

            return JsonResponse({"correct": user_answer == correct_answer})

        except Question.DoesNotExist:
            return JsonResponse({"error": "Question not found"}, status=404)

    return JsonResponse({"error": "Invalid request"}, status=400)

