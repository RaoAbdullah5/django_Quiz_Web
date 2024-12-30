from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# quiz modelcreated
class quiz(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

# question model
class question(models.Model):
    quiz = models.ForeignKey(quiz, related_name='questions', on_delete=models.CASCADE)
    text = models.TextField()
    choice1 = models.CharField(max_length=200)
    choice2 = models.CharField(max_length=200)
    choice3 = models.CharField(max_length=200)
    choice4 = models.CharField(max_length=200)
    correct_choice = models.IntegerField()  # 1, 2, 3, or 4

    def __str__(self):
        return self.text

# user quiz apply
class UserQuizResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(quiz, on_delete=models.CASCADE)
    score = models.IntegerField()
    Total_marks = models.IntegerField()
    completion_time = models.DateTimeField(auto_now_add=True)