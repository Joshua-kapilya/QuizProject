from django.urls import path
from .views import select_quiz_mode, get_questions  # Only import existing views
from. import views

urlpatterns = [
    path('', views.home, name='home'),  # Home - Select Subject
    path('quiz-mode/<int:subject_id>/', select_quiz_mode, name='select_quiz_mode'),  # Select past paper or random
    path('questions/<int:subject_id>/', get_questions, name='get_questions'),  # Display questions
    path("check-answer/", views.check_answer, name="check_answer"),
    path('get_explanation/<int:question_id>/', views.get_explanation, name='get_explanation')
]
