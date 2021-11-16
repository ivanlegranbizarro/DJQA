from django.urls import path
from . import views

urlpatterns = [
    path('', views.question_list, name='question_list'),
    path('question-detail/<slug:slug>',
         views.question_detail, name='question_detail'),
    path('register-question', views.register_question, name='register_question'),
    path('update-question/<slug:slug>',
         views.update_question, name='update_question'),
    path('delete-question/<slug:slug>',
         views.delete_question, name='delete_question'),
    path('update-answer/<int:id>', views.update_answer, name='update_answer'),
    path('delete-answer/<int:id>', views.delete_answer, name='delete_answer'),
    path('edit-profile', views.edit_profile, name='edit_profile'),
    path('list-by-author', views.list_questions_and_answers_by_author,
         name='list_by_author'),
]
