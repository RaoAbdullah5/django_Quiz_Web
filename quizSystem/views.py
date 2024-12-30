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
    total=0
    for question in questions:
        total +=1
        correct_choice = question.correct_choice
        user_answer = answers.get(f'question_{question.id}')
        if str(correct_choice) == user_answer:
            score += 1
    
    return score, total

@login_required
def previous_results(request):
    # Filter the UserQuizResult model by the logged-in user
    results = UserQuizResult.objects.filter(user=request.user)

    # Calculate the percentage directly inside the context
    for result in results:
        result.percentage = int((result.score / result.Total_marks) * 100) if result.Total_marks > 0 else 0

    # Pass the results to the template directly
    context = {
        'results': results  # Context variable with all quiz results
    }

    # Render the page with the provided context
    return render(request, 'previous_results.html', context)

# To show quiz to users and get answers from user then call calculate function
@login_required
def quiz_detail(request, quiz_id):
    quizz = get_object_or_404(quiz, id=quiz_id)
    questions = quizz.questions.all()  # Use related_name='questions' from the model
    if UserQuizResult.objects.filter(user=request.user, quiz=quizz).exists():
        res = UserQuizResult.objects.filter(user=request.user, quiz=quizz).first()
        score=res.score
        total=res.Total_marks
        percentage= int((score/total)*100)
        return render(request, 'quiz_already_attempted.html', {'quiz': quizz, 'res':res.score, 'total':res.Total_marks, 'percent':percentage })
    if request.method == "POST":
        form = QuizForm(request.POST, questions=questions)
        if form.is_valid():
            # Extract user answers from the form
            answers = form.cleaned_data

            # Calculate score
            score, total = calculate_score(answers, questions)

            # Save the result
            UserQuizResult.objects.create(user=request.user, quiz=quizz, score=score, Total_marks= total)

            # Redirect to a result page (passing quiz_id and score)
            return redirect('quiz_result', quiz_id=quiz_id, score=score, totals=total)
    else:
        form = QuizForm(questions=questions)

    return render(request, 'quiz_detail.html', {'quiz': quizz, 'form': form})

# Showing result of quiz
@login_required
def quiz_result(request, quiz_id, score, totals):
    quizz = get_object_or_404(quiz, id=quiz_id)  # Use quiz_id directly here
    percentage= int((score/totals)*100)
    return render(request, 'quiz_result.html', {'quiz': quizz, 'score': score, 'total': totals,'percent':percentage})
