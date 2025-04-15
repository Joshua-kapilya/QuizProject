from django.db import models
from ckeditor.fields import RichTextField

class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class PastPaper(models.Model):
    year = models.IntegerField(unique=True)

    def __str__(self):
        return f"Past Paper {self.year}"
class Question(models.Model):
    TEXT = 'text'
    IMAGE = 'image'

    QUESTION_TYPE_CHOICES = [
        (TEXT, 'Text'),
        (IMAGE, 'Image'),
    ]

    question_number = models.IntegerField(null=True)

    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    past_paper = models.ForeignKey(PastPaper, on_delete=models.CASCADE, null=True, blank=True)
    question_type = models.CharField(max_length=5, choices=QUESTION_TYPE_CHOICES, default=TEXT)
    
    text = models.TextField(null=True, blank=True)  # For text-based questions
    text1 = RichTextField(null=True, blank=True)
    diagram = models.ImageField(upload_to='diagrams/', null=True, blank=True,)  # For image-based questions
    explanation = models.TextField(blank=True)
    explanation1 = RichTextField(null=True, blank=True)

        # Answer choices
    option_a = models.CharField(max_length=250)
    option_b = models.CharField(max_length=250)
    option_c = models.CharField(max_length=250)
    option_d = models.CharField(max_length=250)

    # Store the correct answer as A, B, C, or D, and map to respective options
    correct_answer = models.CharField(
        max_length=1,
        choices=[
            ('A', 'option_a'),
            ('B', 'option_b'),
            ('C', 'option_c'),
            ('D', 'option_d')
        ],
        default='A'  # Defaulting to 'A' to avoid migration errors
    )


    def __str__(self):
        return f" {self.subject.name, self.question_number} - {self.past_paper.year if self.past_paper else 'Random'}: {self.text[:50]}"

