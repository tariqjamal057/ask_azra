from django.urls import path

from .views import (
    AnswerCreateView,
    AnswerDeleteView,
    AnswerUpdateView,
    HomeView,
    LikeAnswerView,
    QuestionCreateView,
    QuestionDeleteView,
    QuestionDetailView,
    QuestionUpdateView,
)

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("question/<int:pk>/", QuestionDetailView.as_view(), name="question-detail"),
    path("question/new/", QuestionCreateView.as_view(), name="ask-question"),
    path("question/<int:pk>/update/", QuestionUpdateView.as_view(), name="question-update"),
    path("question/<int:pk>/delete/", QuestionDeleteView.as_view(), name="question-delete"),
    path("question/<int:pk>/answer/", AnswerCreateView.as_view(), name="add-answer"),
    path("answer/<int:pk>/update/", AnswerUpdateView.as_view(), name="answer-update"),
    path("answer/<int:pk>/delete/", AnswerDeleteView.as_view(), name="answer-delete"),
    path("answer/<int:pk>/like/", LikeAnswerView.as_view(), name="like-answer"),
]
