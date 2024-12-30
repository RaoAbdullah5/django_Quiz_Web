from django.urls import path
from . import views

urlpatterns = [
    path('', views.quiz_list, name='quiz_list'),
    path('prevoius_results', views.previous_results, name='prevoius_results'),
    path('<int:quiz_id>/', views.quiz_detail, name='quiz_detail'),
    # path('<int:quiz_id>/result/<int:score>/', views.quiz_result, name='quiz_result'),
    path('<int:quiz_id>/result/<int:score>/<int:totals>/', views.quiz_result, name='quiz_result'),

]
