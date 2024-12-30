from django.contrib import admin
from .models import quiz, question, UserQuizResult

# # Basic registration
# admin.site.register(quiz)
# admin.site.register(question)
# admin.site.register(UserQuizResult)

class quizAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')  # Fields to display in the list view
    search_fields = ('title',)  # Add search functionality

class questionAdmin(admin.ModelAdmin):
    list_display = ('text', 'quiz', 'correct_choice')
    list_filter = ('quiz',)  # Filter by quiz in the sidebar

class UserQuizResultAdmin(admin.ModelAdmin):
    list_display = ('user', 'quiz', 'score','Total_marks', 'completion_time')
    list_filter = ('quiz',)
    search_fields = ('user__username',)  # Search by username

# Registering models with custom ModelAdmin
admin.site.register(quiz, quizAdmin)
admin.site.register(question, questionAdmin)
admin.site.register(UserQuizResult, UserQuizResultAdmin)

