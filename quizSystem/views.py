from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import quiz, question, UserQuizResult
from .forms import QuizForm

# Quizzes present
def quiz_list(request):
    quizzes = quiz.objects.all()
    return render(request, 'quiz_list.html', {'quizzes': quizzes})

# Function to calculate results

def calculate_score(answers, questions):
    score = 0
    for question in questions:
        correct_choice = question.correct_choice
        user_answer = answers.get(f'question_{question.id}')
        if str(correct_choice) == user_answer:
            score += 1
    return score

# To show quiz to users and get answers from user then call calculate function
@login_required
def quiz_detail(request, quiz_id):
    quizz = get_object_or_404(quiz, id=quiz_id)
    questions = quizz.questions.all()  # Use related_name='questions' from the model
    if UserQuizResult.objects.filter(user=request.user, quiz=quizz).exists():
        return render(request, 'quiz_already_attempted.html', {'quiz': quizz})
    if request.method == "POST":
        form = QuizForm(request.POST, questions=questions)
        if form.is_valid():
            # Extract user answers from the form
            answers = form.cleaned_data

            # Calculate score
            score = calculate_score(answers, questions)

            # Save the result
            UserQuizResult.objects.create(user=request.user, quiz=quizz, score=score)

            # Redirect to a result page (passing quiz_id and score)
            return redirect('quiz_result', quiz_id=quiz_id, score=score)
    else:
        form = QuizForm(questions=questions)

    return render(request, 'quiz_detail.html', {'quiz': quizz, 'form': form})

# Showing result of quiz
@login_required
def quiz_result(request, quiz_id, score):
    quizz = get_object_or_404(quiz, id=quiz_id)  # Use quiz_id directly here
    return render(request, 'quiz_result.html', {'quiz': quizz, 'score': score})
