from django import forms
from .models import question

class QuizForm(forms.Form):
    def __init__(self, *args, **kwargs):
        questions = kwargs.pop('questions')  # Pass questions when initializing the form
        super().__init__(*args, **kwargs)
        for question in questions:
            self.fields[f'question_{question.id}'] = forms.ChoiceField(
                label=question.text,
                choices=[
                    (1, question.choice1),
                    (2, question.choice2),
                    (3, question.choice3),
                    (4, question.choice4),
                ],
                widget=forms.RadioSelect,
            )
